from unittest.mock import Mock, AsyncMock

from pytest import fixture

from src.domain.ports.user_repository import UserRepositoryPort
from src.domain.services.user_service import UserService


@fixture(scope='session')
def user_repository_mock():
    return Mock(spec=UserRepositoryPort)


@fixture(scope='session')
def elastic_search_client_mock():
    return AsyncMock()

@fixture(scope='session')
def user_service_mock():
    return Mock(spec=UserService)