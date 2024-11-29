from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from src.adapters.inbound.restapi.dependencies import user_service_dep
from src.domain.services.user_service import UserService

user_router = APIRouter()

@user_router.get("/")
async def get_users(
        user_service: Annotated[UserService, Depends(user_service_dep)]
):
    return await user_service.list_users()

