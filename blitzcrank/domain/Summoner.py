from typing import Protocol
from dataclasses import dataclass


@dataclass
class Summoner:
    summoner_id: str
    account_id: str
    puuid: str


class SummonerService(Protocol):
    def summoner(self, summoner_id: int) -> Summoner:
        raise NotImplemented

    def create_summoner(self, summoner: Summoner):
        raise NotImplemented
