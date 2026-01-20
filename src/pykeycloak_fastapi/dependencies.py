# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from functools import lru_cache

from fastapi import Depends
from pykeycloak.core.realm import RealmClient
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync
from pykeycloak.services.services import (
    AuthService,
    RolesService,
    SessionsService,
    UmaService,
    UsersService,
)


@lru_cache(1)
def get_in_memory_keycloak_provider() -> KeycloakInMemoryProviderAsync:
    realm_client = RealmClient.from_env()

    return KeycloakInMemoryProviderAsync(realm="realm", realm_client=realm_client)


@lru_cache(1)
def get_keycloak_uma_service(
    provider: KeycloakInMemoryProviderAsync = Depends(get_in_memory_keycloak_provider),
) -> UmaService:
    return UmaService(provider=provider)


@lru_cache(1)
def get_keycloak_auth_service(
    provider: KeycloakInMemoryProviderAsync = Depends(get_in_memory_keycloak_provider),
) -> AuthService:
    return AuthService(provider=provider)


@lru_cache(1)
def get_keycloak_roles_service(
    provider: KeycloakInMemoryProviderAsync = Depends(get_in_memory_keycloak_provider),
) -> RolesService:
    return RolesService(provider=provider)


@lru_cache(1)
def get_keycloak_sessions_service(
    provider: KeycloakInMemoryProviderAsync = Depends(get_in_memory_keycloak_provider),
) -> SessionsService:
    return SessionsService(provider=provider)


@lru_cache(1)
def get_keycloak_users_service(
    provider: KeycloakInMemoryProviderAsync = Depends(get_in_memory_keycloak_provider),
) -> UsersService:
    return UsersService(provider=provider)
