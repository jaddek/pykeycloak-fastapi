# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from typing import Annotated, TypeAlias

from fastapi import Depends

from .dependencies import get_keycloak_registry
from .registries import FactoryRegistry

KeycloakRegistryAlias: TypeAlias = Annotated[  # noqa: UP040
    FactoryRegistry, Depends(get_keycloak_registry)
]
