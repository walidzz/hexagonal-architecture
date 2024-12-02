from src.domain.models.user import User
from src.domain.ports.user_repository import UserRepositoryPort


class UserService:

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    async def list_users(self) -> list[User]:
        # Business logic here
        # For now, just return the list of users from the repository
        return await self.user_repository.list_users()