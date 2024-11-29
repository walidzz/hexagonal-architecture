import pytest
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport
from pytest import fixture

from src.adapters.inbound.restapi import app
from src.adapters.inbound.restapi.dependencies import user_service_dep
from src.domain.models.user import User
from src.domain.services.user_service import UserService


@fixture(scope='session')
def fast_api_app(user_service_mock: UserService):
    app.dependency_overrides[user_service_dep] = lambda: user_service_mock
    yield app
    app.dependency_overrides.clear()

@pytest.mark.asyncio
class TestUsersApiRoutes:
    async def test_get_users(self,fast_api_app: FastAPI, user_service_mock: UserService):
        # GIVEN
        user_service_mock.list_users.return_value = [
            User(
                first_name='John',
                last_name='Doe',
                age=30,
            ),
            User(
                first_name='Jane',
                last_name='Doe',
                age=25,
            ),
        ]
        # WHEN
        async with AsyncClient(transport=ASGITransport(app=fast_api_app, raise_app_exceptions=False), base_url="http://test") as client:
            response = await client.get("/users/")
        # THEN
        assert response.status_code == 200
        assert response.json() == [
            {
                'first_name': 'John',
                'last_name': 'Doe',
                'age': 30,
            },
            {
                'first_name': 'Jane',
                'last_name': 'Doe',
                'age': 25,
            },
        ]

