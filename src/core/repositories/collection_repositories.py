from datetime import datetime
from typing import Sequence, List, Any

from sqlalchemy import func, distinct, Row
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import UUID

from src.core.db.enums.status import Status
from src.core.db.models import Collection, CollectionLink
from src.core.schemas.collection import CollectionFindAllSchema, CollectionFindOneSchema


class CollectionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_collections_paginated_by_account_id(self, account_id: UUID, 
                                                       page: int, page_size: int) \
            -> List[CollectionFindAllSchema]:
        """
        Find all collections by the given account ID
        """
        offset = (page - 1) * page_size

        result = await self.session.execute(
            select(
                Collection.id,
                Collection.name,
                Collection.created_at,
                func.count(CollectionLink.link_id).label("links_count"),
            )
            .outerjoin(CollectionLink, Collection.id == CollectionLink.collection_id)
            .where(
                Collection.account_id == account_id,
                Collection.activity_status == Status.ACTIVE,
            )
            .group_by(Collection.id)
            .limit(page_size)
            .offset(offset)
            .order_by(Collection.created_at.desc())
        )
        return result.mappings().all()
    
    async def count_collections_by_account_id(self, account_id: UUID) -> int:
        """
        Count total collections by the given account ID
        """
        result = await self.session.execute(
            select(
                func.count(Collection.id)
            )
            .where(
                Collection.account_id == account_id,
                Collection.activity_status == Status.ACTIVE,

            )
        )
        return result.scalar_one()

    async def create(self, collection: Collection) -> Collection:
        """
        Create a new collection
        """
        self.session.add(collection)
        await self.session.commit()
        await self.session.refresh(collection)
        return collection

    async def find_collection_by_id(self, collection_id: UUID) -> Collection:
        """
        Find a collection by its ID
        """
        result = await self.session.execute(
            select(Collection)
            .where(Collection.id == collection_id)
        )
        return result.scalar_one_or_none()

    async def find_collection_specific_data_by_id(self, collection_id: UUID) -> CollectionFindOneSchema | None:
        """
        Find a collection by its ID
        """
        result = await self.session.execute(
            select(
                Collection.id,
                Collection.name,
                Collection.created_at,
                func.count(CollectionLink.link_id).label("links_count"),
            )
            .outerjoin(CollectionLink, Collection.id == CollectionLink.collection_id)
            .where(
                Collection.id == collection_id,
            )
            .group_by(Collection.id)
        )
        return result.one_or_none()

    async def save(self, collection: Collection) -> None:
        """
        Save a collection
        """
        await self.session.commit()
        await self.session.refresh(collection)