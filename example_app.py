import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException

from pykeycloak_fastapi.aliases import KeycloakUsersService


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.environ.setdefault("KEYCLOAK_SERVER_URL", "http://localhost:8080")
    os.environ.setdefault("KEYCLOAK_REALM", "myrealm")
    os.environ.setdefault("KEYCLOAK_CLIENT_ID", "myclient")
    os.environ.setdefault("KEYCLOAK_CLIENT_SECRET", "mysecret")

    yield
    pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to pykeycloak-fastapi example app!"}


@app.get("/users")
async def get_users(users_service: KeycloakUsersService):
    try:
        users = await users_service.get_users_async()
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch users: {str(e)}")  # noqa: B904


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # noqa: S104
