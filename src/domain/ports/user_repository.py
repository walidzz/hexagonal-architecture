from abc import ABC, abstractmethod

from src.domain.models.user import User


class UserRepositoryPort(ABC):

    @abstractmethod
    async def list_users(self) -> list[User]:
        pass