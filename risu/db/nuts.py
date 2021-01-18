from typing import List, Set

from risu.db.holotools import get_live
from risu.models import Holotools

class Nuts:
    def __init__(self):
        # self._tentacles = dict()
        self._live: Set[Holotools] = set()
        self._taken: Set[Holotools] = set()
        self._not_taken: Set[Holotools] = set()


    async def refresh_live(self):
        live_now = set(await get_live())
        ended = self._live - live_now
        new = live_now - self._live
        self._live = live_now
        for stream in ended:
            if stream in self._taken:
                # TODO tell action to stop
                self._taken.remove(stream)
            if stream in self._not_taken:
                self._not_taken.remove(stream)
        self._not_taken.update(new)
