
from fastapi import FastAPI

from src.adapters.inbound.restapi.users import user_router

app = FastAPI()



app.include_router(user_router, prefix="/users", tags=["users"])