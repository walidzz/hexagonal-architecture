from elasticsearch import AsyncElasticsearch

from src.domain.models.user import User
from src.domain.ports.user_repository import UserRepositoryPort


class LocalObjectUserRepository(UserRepositoryPort):
    def __init__(self, users: list[dict]):
        self.users = users

    async def list_users(self) -> list[User]:
        return [User.model_validate(user) for user in self.users]


class ElasticSearchUserRepository(UserRepositoryPort):
    def __init__(self, es_client: AsyncElasticsearch):
        self._es_client = es_client

    async def list_users(self) -> list[User]:
        result = await self._es_client.search(index='users')
        return [
            User.model_validate(user["_source"]) for user in result['hits']['hits']
        ]