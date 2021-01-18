from typing import Optional

from pydantic import BaseModel, Field

yt = "https://www.youtube.com/watch?v="


class Holotools(BaseModel):
    name: str
    status: str
    start: Optional[str]
    link: Optional[str]

    def __hash__(self) -> int:
        return hash(self.link)


class Tentacle(BaseModel):
    uid: str
    start: Optional[str]

    def __hash__(self) -> int:
        return hash(self.uid)


class TentacleStatus(BaseModel):
    status: str = Field(..., description="start|stop|wait|continue")
    stream: Optional[Holotools]
