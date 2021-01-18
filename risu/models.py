from typing import Optional

from pydantic import BaseModel

yt = "https://www.youtube.com/watch?v="

class Holotools(BaseModel):
    name: str
    status: str
    start: Optional[str]
    link: Optional[str]
