from collections.abc import Callable
from typing import Annotated

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from src.domain.ports.user_repository import UserRepositoryPort
from src.domain.services.user_service import UserService
from src.adapters.outbound.user_repository import LocalObjectUserRepository, ElasticSearchUserRepository


def local_user_repository_dep() -> LocalObjectUserRepository:
    return LocalObjectUserRepository(
        users=[
            {"first_name": "John", "last_name": "Doe", "age": 30},
            {"first_name": "Jane", "last_name": "Doe", "age": 25},
        ]
    )

def elastic_search_user_repository_dep() -> ElasticSearchUserRepository:
    return ElasticSearchUserRepository(
        es_client=AsyncElasticsearch(
            hosts=['http://localhost:9200'],
            api_key="N0hYeGM1TUJZSE1OejVtcVB3blc6TnZFckhSZktST3l1ZHdMNEd3SVhoQQ=="
        )
    )


def user_service_dep(
        user_repository_factory: Callable[[], UserRepositoryPort] = local_user_repository_dep
) -> UserService:
    return UserService(
        user_repository=user_repository_factory()
    )