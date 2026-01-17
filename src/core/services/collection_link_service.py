from uuid import UUID

from src.core.db.models import CollectionLink
from src.core.repositories.collection_link_repository import CollectionLinkRepository


class CollectionLinkService:
    def __init__(self, collection_link_repository: CollectionLinkRepository):
        self.collection_link_repository = collection_link_repository

    async def get_collection_link_by_collection_id_and_link_id(self,
                                                         collection_id: UUID,
                                                         link_id: UUID) -> CollectionLink:
        return await self.collection_link_repository.find_by_collection_id_and_link_id(collection_id, link_id)