from typing import List

from sqlalchemy import func
from sqlalchemy.future import select
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.enums.status import Status
from src.core.db.models import Link, CollectionLink
from src.core.schemas.link import LinkFindAllSchema


class LinkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_links_paginated_by_collection_id(
            self, collection_id: UUID, page: int, page_size: int
    ) -> List[LinkFindAllSchema]:
        """
        Find all links by the given collection ID
        """
        offset = (page - 1) * page_size

        result = await self.session.execute(
            select(
                Link.id,
                Link.url,
            )
            .join(CollectionLink, Link.id == CollectionLink.link_id)
            .where(
                CollectionLink.collection_id == collection_id,
                Link.status == Status.ACTIVE,
                CollectionLink.activity_status == Status.ACTIVE,
            )
            .limit(page_size)
            .offset(offset)
        )

        rows = result.mappings().all()
        return [LinkFindAllSchema(**row) for row in rows]

    async def count_links_by_collection_id(self, collection_id: UUID) -> int:
        """
        Count total links by the given account ID
        """
        result = await self.session.execute(
            select(func.count(Link.id))
            .join(CollectionLink, Link.id == CollectionLink.link_id)
            .where(
                CollectionLink.collection_id == collection_id,
                Link.status == Status.ACTIVE,
            )
        )
        return result.scalar_one()

    async def create(self, link: Link) -> Link:
        """
        Create a new link
        """
        self.session.add(link)
        await self.session.commit()
        await self.session.refresh(link)
        return link

    async def get_by_url(self, url: str) -> Link | None:
        """
        Get link by url
        """
        result = await self.session.execute(
            select(Link).where(Link.url == url)
        )
        return result.scalar_one_or_none()

    async def get_by_id(self, link_id: UUID) -> Link | None:
        """
        Get link by id
        """
        result = await self.session.execute(
            select(Link).where(Link.id == link_id)
        )
        return result.scalar_one_or_none()

    async def save(self):
        """
        Save an existing link
        """
        await self.session.commit()

