# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from typing import cast

from starlette.requests import Request

from pykeycloak_fastapi.registries import FactoryRegistry


def get_keycloak_registry(request: Request) -> FactoryRegistry:
    return cast(FactoryRegistry, request.app.state.keycloak)
