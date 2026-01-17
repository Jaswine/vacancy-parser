from typing import List
from uuid import UUID
import logging

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.enums.status import Status
from src.core.db.models import Link, CollectionLink
from src.core.repositories.collection_link_repository import CollectionLinkRepository
from src.core.repositories.link_repository import LinkRepository
from src.core.schemas.link import LinkFindAllSchema

logger = logging.getLogger(__name__)

class LinkService:
    def __init__(
        self,
        session: AsyncSession,
        link_repository: LinkRepository,
        collection_link_repository: CollectionLinkRepository,
    ) -> None:
        self.session = session
        self.link_repository = link_repository
        self.collection_link_repository = collection_link_repository

    async def find_links_paginated_by_collection_id(
        self, collection_id: UUID, page: int, page_size: int
    ) -> List[LinkFindAllSchema]:
        """
        Find all links by the given collection ID
        """
        return await self.link_repository.find_links_paginated_by_collection_id(
            collection_id, page, page_size
        )

    async def count_links_by_collection_id(self, collection_id: UUID) -> int:
        """
        Count the number of links by the given collection ID
        """
        return await self.link_repository.count_links_by_collection_id(collection_id)

    async def create(self, collection_id: UUID, url: str) -> Link:
        """
        Create a new link
        """

        # !!!: Rewrite, create a transaction

        # Check if link exists
        link = await self.link_repository.get_by_url(url)

        if link:
            # Reactivate if ARCHIVED
            if link.status == Status.ARCHIVED:
                link.status = Status.ACTIVE
        else:
            # Create new link
            link = Link(url=url)
            link = await self.link_repository.create(link)

        # Attach link to collection if not already attached
        attached: (
            CollectionLink | None
        ) = await self.collection_link_repository.find_by_collection_id_and_link_id(
            collection_id, link.id
        )
        if attached:
            if attached.activity_status == Status.ARCHIVED:
                attached.activity_status = Status.ACTIVE
                await self.collection_link_repository.save()
        else:
            await self.collection_link_repository.create(
                CollectionLink(collection_id=collection_id, link_id=link.id)
            )

        return link

    async def get_link_by_id(self, link_id: UUID) -> Link | None:
        """
        Get link by id
        """
        return await self.link_repository.get_by_id(link_id)

    async def remove(self, collection_link: CollectionLink):
        """
        Remove a link
        """
        collection_link.activity_status = Status.ARCHIVED
        await self.collection_link_repository.save()
