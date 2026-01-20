# pykeycloak-fastapi

FastAPI integration layer for pykeycloak - a Python client for Keycloak authentication and authorization services.

## Features

- FastAPI dependency injection for Keycloak services
- Pre-configured service aliases for easy integration
- Support for UMA, Auth, Roles, Sessions, and Users services
- Async-ready implementation
- Type hints for better developer experience

## Installation

```bash
pip install pykeycloak-fastapi
```

## Quick Start

```python
from fastapi import FastAPI, Depends, HTTPException
from pykeycloak_fastapi.aliases import KeycloakAuthServiceAlias, KeycloakUsersServiceAlias

app = FastAPI()

@app.get("/protected")
async def protected_endpoint(auth_service: KeycloakAuthServiceAlias):
    # Example of using the auth service
    # You would typically validate tokens here
    return {"message": "Access granted"}

@app.get("/users")
async def get_users(users_service: KeycloakUsersServiceAlias):
    # Example of using the users service
    try:
        users = await users_service.get_users()
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Dependencies

This package relies on:
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs with Python
- [pykeycloak](https://github.com/jaddek/pykeycloak) - Python client for Keycloak

## Configuration

The package uses environment variables for Keycloak configuration via `RealmClient.from_env()`.

## Services Available

The package provides the following Keycloak services as FastAPI dependencies:
- `KeycloakAuthServiceAlias` - Authentication service
- `KeycloakUmaServiceAlias` - User-Managed Access service
- `KeycloakRolesServiceAlias` - Roles management service
- `KeycloakSessionsServiceAlias` - Sessions management service
- `KeycloakUsersServiceAlias` - Users management service

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.