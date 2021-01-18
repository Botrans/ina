import time
from typing import List, Optional, Set

from risu.db.holotools import get_live
from risu.models import Holotools, Tentacle, TentacleStatus


class Nuts:
    """
    Not threadsafe.

    Use asyncronously
    """

    refresh_min = 5

    def __init__(self):
        self._live: Set[Holotools] = set()
        self._taken: Set[Holotools] = set()
        self._not_taken: Set[Holotools] = set()
        self._tentacles: Dict[Tentacle, Holotools] = dict()
        self._ended: Set[Holotools] = set()
        self._last_refresh = time.time() - self.refresh_min

    def tentacle_needed(self) -> bool:
        return len(self._not_taken) > 0

    def add_tentacle(self, tentacle: Tentacle) -> Optional[Holotools]:
        if self.tentacle_needed():
            holo = next(iter(self._not_taken))
            self._not_taken.remove(holo)
            self._taken.add(holo)
            self._tentacles[tentacle] = holo
            return holo
        return None

    def tentacle_status(self, tentacle: Tentacle) -> TentacleStatus:
        if tentacle in self._tentacles:
            if self._tentacles[tentacle] in self._ended:
                return TentacleStatus(status="stop")
            return TentacleStatus(status="continue")
        if self.tentacle_needed():
            return TentacleStatus(status="start", stream=self.add_tentacle(tentacle))
        return TentacleStatus(status="wait")

    async def refresh_live(self) -> None:
        if time.time() - self._last_refresh < self.refresh_min:
            return None
        self._last_refresh = time.time()

        live_now = set(await get_live())
        ended = self._live - live_now
        new = live_now - self._live
        self._live = live_now
        for stream in ended:
            if stream in self._taken:
                self._ended.add(stream)
                self._taken.remove(stream)
            if stream in self._not_taken:
                self._not_taken.remove(stream)
        self._not_taken.update(new)
