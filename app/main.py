from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .routers import games, publishers

app = FastAPI()

app.include_router(games.router)
app.include_router(publishers.router)

@app.get("/")
async def root():
    return {"message": "Welcome to this simple FastAPI Project! Check out the games in /games, or their publishers in /publishers!"}