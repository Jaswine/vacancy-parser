import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.auth import get_current_user_payload
from src.api.schemas.collection import (
    CollectionFindAllPaginationSchema,
    CollectionCreateSchema,
    CollectionCreateData,
    CollectionFindOneSchema,
    CollectionUpdateNameData,
)
from src.core.schemas.collection import CollectionFindAllSchema
from src.api.schemas.message import MessageSuccess
from src.core.db.database import get_db
from src.core.repositories.collection_repositories import CollectionRepository
from src.core.services.collection_services import CollectionService
from src.core.db.models import Collection

router = APIRouter(prefix="/collections", tags=["Collection"])

logger = logging.getLogger(__name__)


# -------------------------
# Show all users' collections
# -------------------------
@router.get("", response_model=CollectionFindAllPaginationSchema)
async def show_collection(
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    service: CollectionService = CollectionService(collection_repository)

    # Get account ID from payload
    account_id = payload["sub"]

    try:
        # Get total collections count
        total_collections = await service.get_total_collections_count(account_id)

        # Get paginated collections
        collections: List[CollectionFindAllSchema] = await service.find_collections_paginated_by_account_id(
            account_id, page, page_size
        )

        # Build and return response
        return CollectionFindAllPaginationSchema(
            page=page, page_size=page_size, total=total_collections, items=collections
        )
    except Exception:
        logger.exception(
            "❌ Unexpected error during finding all collections",
            extra={"id": account_id},
        )
        raise


# -------------------------
# Create a new collection
# -------------------------
@router.post("", response_model=CollectionCreateSchema)
async def create_collection(
    collection_data: CollectionCreateData,
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    service: CollectionService = CollectionService(collection_repository)

    # Get account ID from payload
    account_id = payload["sub"]

    try:
        # Create and return new collection
        return await service.create_collection(account_id, collection_data.name)
    except Exception:
        logger.exception(
            "❌ Unexpected error",
            extra={"id": account_id},
        )
        raise


# -------------------------
# Get collection by id
# -------------------------
@router.get("/{collection_id}", response_model=CollectionFindOneSchema)
async def get_collection_by_id(
    collection_id: UUID,
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    service: CollectionService = CollectionService(collection_repository)

    try:
        return await service.find_collection_specific_data_by_id(collection_id)
    except Exception:
        logger.exception(
            "❌ Unexpected error",
            extra={"id": collection_id},
        )
        raise


# -------------------------
# Update collection's name by id
# -------------------------
@router.patch("/{collection_id}", response_model=MessageSuccess)
async def update_collection(
    collection_id: UUID,
    collection_data: CollectionUpdateNameData,
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    service: CollectionService = CollectionService(collection_repository)

    try:
        # Get collection by id
        collection: Collection | None = await service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        if not collection_data.name.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Collection name cannot be empty",
            )

        if collection.name == collection_data.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New collection name must be different",
            )

        # Update collection's name
        await service.update_collection_name(collection, collection_data.name)

        return MessageSuccess(
            message="Collection name has been updated successfully!",
        )
    except Exception:
        logger.exception(
            "❌ Unexpected error",
            extra={"id": collection_id},
        )
        raise


# -------------------------
# Remove collection by id
# -------------------------
@router.delete("/{collection_id}")
async def remove_collection(
    collection_id: UUID,
    payload: dict = Depends(get_current_user_payload),
    db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    service: CollectionService = CollectionService(collection_repository)

    try:
        # Get collection by id
        collection: Collection | None = await service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        # Remove collection's name
        await service.remove_collection(collection)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception:
        logger.exception(
            "❌ Unexpected error",
            extra={"id": collection_id},
        )
        raise
