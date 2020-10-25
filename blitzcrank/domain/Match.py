from typing import List
from dataclasses import dataclass
import datetime

from blitzcrank.domain.Team import Team


@dataclass
class Match:
    match_id: int
    creation_date: datetime
    duration: int
    game_type: str
    mode: str
    queue_id: int
    season_id: int
    version: str

    team: List[Team]
