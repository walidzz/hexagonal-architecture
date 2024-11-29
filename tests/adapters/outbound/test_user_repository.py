import pytest

from src.adapters.outbound.user_repository import LocalObjectUserRepository, ElasticSearchUserRepository
from src.domain.models.user import User

@pytest.mark.asyncio
class TestLocalObjectUserRepository:
    async def test_list_users(self):
        # GIVEN
        users = [
            {"first_name": "John", "last_name": "Doe", "age": 30},
            {"first_name": "Jane", "last_name": "Doe", "age": 25},
        ]
        # WHEN
        user_repository = LocalObjectUserRepository(users=users)
        # THEN
        assert await user_repository.list_users() == [
           User.model_validate(u) for u in users
        ]

@pytest.mark.asyncio
class TestElasticSearchUserRepository:
    async def test_list_users(self, elastic_search_client_mock):
        # GIVEN
        elastic_search_client_mock.search.return_value = {
            'hits': {
                'hits': [
                    {"_source": {"first_name": "John", "last_name": "Doe", "age": 30}},
                    {"_source": {"first_name": "Jane", "last_name": "Doe", "age": 25}},
                ]
            }
        }
        # WHEN
        user_repository = ElasticSearchUserRepository(es_client=elastic_search_client_mock)
        # THEN
        assert await user_repository.list_users() == [
            User.model_validate({"first_name": "John", "last_name": "Doe", "age": 30}),
            User.model_validate({"first_name": "Jane", "last_name": "Doe", "age": 25}),
        ]

