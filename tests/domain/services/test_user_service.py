import pytest

from src.domain.models.user import User
from src.domain.services.user_service import UserService

@pytest.mark.asyncio
class TestUserService:
    async def test_list_users(self, user_repository_mock):
        # Given
        user_repository_mock.list_users.return_value = [
            User(
                first_name='John',
                last_name='Doe',
                age=30,
            )
        ]
        user_service = UserService(user_repository=user_repository_mock)
        # When
        result = await user_service.list_users()
        # Then
        assert result == [
            User(
                first_name='John',
                last_name='Doe',
                age=30,
            )
        ]
        user_repository_mock.list_users.assert_called_once()