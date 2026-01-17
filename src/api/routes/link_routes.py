import logging
from typing import List, Collection
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.dependencies.auth import get_current_user_payload
from src.api.schemas.link import LinkFindAllPaginationSchema, LinkDataSchema, LinkSchema
from src.core.db.database import get_db
from src.core.db.models import Link
from src.core.repositories.collection_link_repository import CollectionLinkRepository
from src.core.repositories.collection_repository import CollectionRepository
from src.core.repositories.link_repository import LinkRepository
from src.core.schemas.link import LinkFindAllSchema
from src.core.services import collection_service
from src.core.services.collection_link_service import CollectionLinkService
from src.core.services.collection_service import CollectionService
from src.core.services.link_service import LinkService

router = APIRouter(prefix="/collections", tags=["Link"])

logger = logging.getLogger(__name__)


# -------------------------
# Show all links' collections
# -------------------------
@router.get("/{collection_id}/links", response_model=LinkFindAllPaginationSchema)
async def get_all_links(
        collection_id: UUID,
        payload: dict = Depends(get_current_user_payload),
        db: AsyncSession = Depends(get_db),
        page: int = Query(1, ge=1, description="Page number"),
        page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    collection_service: CollectionService = CollectionService(collection_repository)

    link_repository: LinkRepository = LinkRepository(db)
    collection_link_repository: CollectionLinkRepository = CollectionLinkRepository(db)
    service: LinkService = LinkService(db, link_repository, collection_link_repository)

    try:
        # Get collection by id
        collection: Collection | None = await collection_service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        # Get total links count
        links_count: int = await service.count_links_by_collection_id(collection_id)

        # Get paginated links
        links: List[LinkFindAllSchema] = await service.find_links_paginated_by_collection_id(
            collection_id, page, page_size
        )

        # Build and return response
        return LinkFindAllPaginationSchema(
            page=page,
            page_size=page_size,
            total=links_count,
            items=links
        )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err)
        )


# -------------------------
# Create a new link
# -------------------------
@router.post("/{collection_id}/links",
             response_model=LinkSchema, status_code=status.HTTP_201_CREATED)
async def create_link(
        collection_id: UUID,
        collection_data: LinkDataSchema,
        payload: dict = Depends(get_current_user_payload),
        db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    collection_service: CollectionService = CollectionService(collection_repository)

    link_repository: LinkRepository = LinkRepository(db)
    collection_link_repository: CollectionLinkRepository = CollectionLinkRepository(db)
    link_service: LinkService = LinkService(db, link_repository, collection_link_repository)

    try:
        # Get collection by id
        collection: Collection | None = await collection_service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        # Create and return new link
        return await link_service.create(collection_id, collection_data.url)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err)
        )


# -------------------------
# Remove link by id
# -------------------------
@router.delete("/{collection_id}/links/{link_id}")
async def remove_link(
        collection_id: UUID,
        link_id: UUID,
        payload: dict = Depends(get_current_user_payload),
        db: AsyncSession = Depends(get_db),
):
    collection_repository: CollectionRepository = CollectionRepository(db)
    collection_service: CollectionService = CollectionService(collection_repository)

    link_repository: LinkRepository = LinkRepository(db)
    collection_link_repository: CollectionLinkRepository = CollectionLinkRepository(db)
    link_service: LinkService = LinkService(db, link_repository, collection_link_repository)
    collection_link_service: CollectionLinkService = CollectionLinkService(collection_link_repository)

    try:
        # Get collection by id
        collection: Collection | None = await collection_service.find_collection_by_id(collection_id)
        if not collection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection not found",
            )

        # Get link by id
        link: Link = await link_service.get_link_by_id(link_id)
        if not link:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Link not found",
            )

        collection_link = await collection_link_service.get_collection_link_by_collection_id_and_link_id(collection_id, link_id)
        if not collection_link:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Collection link relationship not found",
            )

        # Create and return new link
        await link_service.remove(collection_link)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(err)
        )
