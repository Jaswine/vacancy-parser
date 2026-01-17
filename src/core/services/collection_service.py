import logging
from typing import List
from uuid import UUID

from src.core.db.enums.status import Status
from src.core.repositories.collection_repository import CollectionRepository
from src.core.db.models import Collection
from src.core.schemas.collection import CollectionFindAllSchema, CollectionFindOneSchema

logger = logging.getLogger(__name__)


class CollectionService:
    def __init__(self, collection_repository: CollectionRepository):
        self.collection_repository = collection_repository

    async def find_collections_paginated_by_account_id(
        self, account_id: UUID, page: int, page_size: int
    ) -> List[CollectionFindAllSchema]:
        """
        Find all collections by the given account ID
        """
        return (
            await self.collection_repository.find_collections_paginated_by_account_id(
                account_id, page, page_size
            )
        )

    async def create_collection(self, account_id: UUID, name: str) -> Collection:
        """
        Create a new collection
        """
        new_collection: Collection = Collection(account_id=account_id, name=name)
        return await self.collection_repository.create(new_collection)

    async def find_collection_by_id(self, collection_id: UUID) -> Collection | None:
        """
        Find a collection by its ID
        """
        return await self.collection_repository.find_collection_by_id(collection_id)

    async def find_collection_specific_data_by_id(
        self, collection_id: UUID
    ) -> CollectionFindOneSchema | None:
        """
        Get a collection by its ID
        """
        return await self.collection_repository.find_collection_specific_data_by_id(
            collection_id
        )

    async def get_total_collections_count(self, account_id: UUID) -> int:
        """
        Get total number of collections for a given account ID
        """
        return await self.collection_repository.count_collections_by_account_id(
            account_id
        )

    async def update_collection_name(self, collection: Collection, name: str) -> None:
        """
        Update the collection name
        """
        collection.name = name
        await self.collection_repository.save(collection)

    async def remove_collection(self, collection: Collection) -> None:
        """
        Remove a collection
        """
        collection.activity_status = Status.ARCHIVED
        await self.collection_repository.save(collection)
