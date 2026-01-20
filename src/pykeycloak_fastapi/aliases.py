# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from typing import Annotated, TypeAlias

from fastapi.params import Depends
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync
from pykeycloak.services.services import UmaService, AuthService, RolesService, SessionsService, UsersService
from .dependencies import (
    get_in_memory_keycloak_provider,
    get_keycloak_uma_service,
    get_keycloak_auth_service,
    get_keycloak_roles_service,
    get_keycloak_sessions_service,
    get_keycloak_users_service
)

KeycloakInMemoryProviderAsyncAlias: TypeAlias = Annotated[
    KeycloakInMemoryProviderAsync, Depends(get_in_memory_keycloak_provider)
]

KeycloakUmaServiceAlias: TypeAlias = Annotated[
    UmaService, Depends(get_keycloak_uma_service)
]

KeycloakAuthServiceAlias: TypeAlias = Annotated[
    AuthService, Depends(get_keycloak_auth_service)
]

KeycloakRolesServiceAlias: TypeAlias = Annotated[
    RolesService, Depends(get_keycloak_roles_service)
]

KeycloakSessionsServiceAlias: TypeAlias = Annotated[
    SessionsService, Depends(get_keycloak_sessions_service)
]

KeycloakUsersServiceAlias: TypeAlias = Annotated[
    UsersService, Depends(get_keycloak_users_service)
]