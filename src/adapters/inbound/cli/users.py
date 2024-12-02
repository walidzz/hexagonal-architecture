from typing import Callable

from src.adapters.inbound.cli.dependencies import user_service_dep
from src.domain.services.user_service import UserService


async def get_users(
        user_service_factory: Callable[ [],UserService] = user_service_dep
):
    user_service = user_service_factory()
    result = await user_service.list_users()
    return [user.model_dump() for user in result]
