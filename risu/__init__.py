from fastapi import FastAPI

from risu.db.nuts import Nuts

app = FastAPI()
nuts = Nuts()


@app.get("/")
async def root():
    return {"message": "Hello World"}
