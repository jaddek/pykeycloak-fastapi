# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Anton "Tony" Nazarov <tonynazarov+dev@gmail.com>

from pykeycloak.core.realm import Realm
from pykeycloak.factories import KeycloakServiceFactory


class FactoryRegistry:
    def __init__(self) -> None:
        self._map: dict[Realm, KeycloakServiceFactory] = {}

    def register(self, realm: Realm, factory: KeycloakServiceFactory) -> None:
        self._map[realm] = factory

    def get(self, realm: Realm) -> KeycloakServiceFactory:
        instance = self._map.get(realm)
        if not instance:
            raise ValueError(f"Provider for realm '{realm.name}' not found")

        return instance

    async def close_all(self) -> None:
        for factory in self._map.values():
            await factory.provider.close()

    @staticmethod
    def from_realm(realm: Realm, factory: KeycloakServiceFactory) -> "FactoryRegistry":
        registry = FactoryRegistry()
        registry.register(realm, factory)

        return registry
