from src.domain.models.user import User
from src.domain.services.user_service import UserService


class TestUserService:
    def test_list_users(self, user_repository_mock):
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
        result = user_service.list_users()
        # Then
        assert result == [
            User(
                first_name='John',
                last_name='Doe',
                age=30,
            )
        ]