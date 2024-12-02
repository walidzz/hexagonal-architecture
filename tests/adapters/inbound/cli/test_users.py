import pytest

from src.adapters.inbound.cli import get_users
from src.domain.models.user import User


@pytest.mark.asyncio
class TestGetUsers:
    async def test_get_users(self, user_service_mock):
        # GIVEN
        user_service_mock.list_users.return_value = [
            User(
                first_name='John',
                last_name='Doe',
                age=30,
            )
        ]
        # WHEN
        result = await get_users(user_service_factory=lambda: user_service_mock)
        # THEN
        assert result == [
            {
                "first_name": "John",
                "last_name": "Doe",
                "age": 30
            }
        ]