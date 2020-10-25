from typing import Protocol, List
from dataclasses import dataclass

from blitzcrank.domain.Rank import Rank


@dataclass
class Incarnation:
    summoner_name: str
    ranks = List[Rank]


class IncarnationService(Protocol):
    def incarnation(self, incarnation_id: int) -> Incarnation:
        raise NotImplemented

    def create_incarnation(self, incarnation: Incarnation):
        raise NotImplemented
