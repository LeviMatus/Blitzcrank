from typing import Protocol, List
from dataclasses import dataclass

from blitzcrank.domain.Participant import Participant


@dataclass
class Team:
    team_id: str
    color: int
    participants: List[Participant]