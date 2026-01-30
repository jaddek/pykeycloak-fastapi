import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pykeycloak.core.realm import Realm
from pykeycloak.dependancies import get_factory
from pykeycloak.providers.providers import KeycloakInMemoryProviderAsync
from starlette.requests import Request

from pykeycloak_fastapi.aliases import KeycloakRegistryAlias
from pykeycloak_fastapi.registries import FactoryRegistry

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("pykeycloak")
logger.setLevel(logging.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    realm, _, factory = get_factory("otago", KeycloakInMemoryProviderAsync)

    app.state.keycloak = registry = FactoryRegistry.from_realm(realm, factory)

    await registry.get(realm).auth.client_login_async()

    yield

    await registry.get(realm).provider.close()


def get_keycloak_registry(request: Request) -> FactoryRegistry:
    return request.app.state.keycloak.registry


app = FastAPI(lifespan=lifespan)


@app.get("/certs")
async def certs(kc: KeycloakRegistryAlias):
    return {"certs": await kc.get(Realm(name="otago")).auth.get_certs_async()}


@app.get("/users")
async def users(kc: KeycloakRegistryAlias):
    return {"users": await kc.get(Realm(name="otago")).users.get_users_async()}
