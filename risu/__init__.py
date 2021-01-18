from fastapi import FastAPI

from risu.db.nuts import Nuts
from risu.models import Tentacle, TentacleStatus

app = FastAPI()
nuts = Nuts()


@app.post("/status")
async def status(tentacle: Tentacle) -> TentacleStatus:
    await nuts.refresh_live()
    return nuts.tentacle_status(tentacle)


@app.get("/")
async def root():
    return {"message": "Hello World"}
