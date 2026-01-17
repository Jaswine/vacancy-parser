from celery.bin.result import result
from sqlalchemy import UUID, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import CollectionLink


class CollectionLinkRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def exists(self, collection_id: UUID, link_id: UUID) -> bool:
        """
        Check if a collection link exists
        """
        result = await self.session.execute(
            select(CollectionLink)
            .where(
                CollectionLink.collection_id == collection_id,
                CollectionLink.link_id == link_id
            )
        )
        return result.scalar_one_or_none() is not None

    async def create(self, collection_link: CollectionLink) -> CollectionLink:
        """
        Create a new collection link
        """
        self.session.add(collection_link)
        await self.session.commit()
        await self.session.refresh(collection_link)
        # await self.session.flush()
        return collection_link

    async def find_by_collection_id_and_link_id(self,
                                                collection_id: UUID,
                                                link_id: UUID) -> CollectionLink | None:
        """
        Find a collection link by collection_id and link_id
        """
        result = await self.session.execute(
            select(CollectionLink)
            .where(
                CollectionLink.collection_id == collection_id,
                CollectionLink.link_id == link_id
            )
        )

        return result.scalar_one_or_none()

    async def save(self):
        """
        Save the collection link
        """
        await self.session.commit()

