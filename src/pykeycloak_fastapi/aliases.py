# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from typing import Annotated

from fastapi import Depends
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync
from pykeycloak.services.services import (
    AuthService,
    RolesService,
    SessionsService,
    UmaService,
    UsersService,
)

from .dependencies import (
    get_in_memory_keycloak_provider,
    get_keycloak_auth_service,
    get_keycloak_roles_service,
    get_keycloak_sessions_service,
    get_keycloak_uma_service,
    get_keycloak_users_service,
)

type KeycloakInMemoryProvider = Annotated[
    KeycloakInMemoryProviderAsync, Depends(get_in_memory_keycloak_provider)
]

type KeycloakUmaService = Annotated[UmaService, Depends(get_keycloak_uma_service)]

type KeycloakAuthService = Annotated[AuthService, Depends(get_keycloak_auth_service)]

type KeycloakRolesService = Annotated[RolesService, Depends(get_keycloak_roles_service)]

type KeycloakSessionsService = Annotated[
    SessionsService, Depends(get_keycloak_sessions_service)
]

type KeycloakUsersService = Annotated[UsersService, Depends(get_keycloak_users_service)]
