from typing import List

from risu.httpaio import session
from risu.models import Holotools

holotools = "https://jetrico.sfo2.digitaloceanspaces.com/hololive/youtube.json"
yt = "https://www.youtube.com/watch?v="

async def get_live() -> List[Holotools]:
    r = await session.request(method="GET", url=holotools)
    json = await r.json()
    return [Holotools(
        name=j["channel"]["name"],
        status=j["status"],
        start=j["live_start"],
        link=f"{yt}{j['yt_video_key']}"
    ) for j in json["live"]]
