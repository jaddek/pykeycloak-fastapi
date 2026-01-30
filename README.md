# pykeycloak-fastapi

FastAPI integration layer for pykeycloak - a Python client for Keycloak authentication and authorization services.

## Features

- FastAPI dependency injection for Keycloak services
- Registry pattern for managing multiple Keycloak realms
- Support for async providers including in-memory implementations
- Pre-configured service aliases for easy integration
- Full async support for non-blocking operations
- Type hints for better developer experience

## Installation

```bash
pip install pykeycloak-fastapi
```

## Quick Start

Here's a complete example showing how to integrate pykeycloak-fastapi with your FastAPI application:

```python
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


@app.get("/resources")
async def resources(kc: KeycloakRegistryAlias):
    # Example of using the authorization service to get resources
    return {"resources": await kc.get(Realm(name="otago")).authz_resource.get_resources_async()}


@app.get("/permissions")
async def permissions(kc: KeycloakRegistryAlias):
    # Example of using the authorization service to get permissions
    return {"permissions": await kc.get(Realm(name="otago")).authz_permission.get_permissions_async()}
```

## Core Concepts

### FactoryRegistry
The `FactoryRegistry` class manages multiple Keycloak service factories by realm. It provides methods to register and retrieve factories for specific realms.

### KeycloakRegistryAlias
The `KeycloakRegistryAlias` is a type alias that combines dependency injection with the registry pattern, allowing easy access to Keycloak services in route handlers.

### Authorization (AuthZ)
The authorization service provides comprehensive access control capabilities including resource registration, permission management, and policy enforcement. It supports both traditional role-based access control and fine-grained authorization through UMA (User-Managed Access) protocols.

### Lifespan Management
The example shows how to properly initialize and clean up Keycloak connections using FastAPI's lifespan context manager.

## Dependencies

This package relies on:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs with Python
- [pykeycloak](https://github.com/jaddek/pykeycloak) - Python client for Keycloak
- [pykeycloak-realm](https://github.com/jaddek/pykeycloak-realm) - Python realm
- [PyYAML](https://pyyaml.org/) - YAML processing
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

## Configuration

The package uses the underlying pykeycloak library's configuration mechanisms. You can configure Keycloak connection settings through environment variables or direct instantiation of Realm objects.

## Services Available

Through the registry pattern, you can access all Keycloak services:
- Authentication service (`auth`)
- Authorization service with UMA support (`uma`)
- User management (`users`)
- Role management (`roles`)
- Session management (`sessions`)
- Clients management (`clients`)
- Authz management (`permissions`, `policies`, `resources`, `scopes`)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Version

Current version: 0.1.1
