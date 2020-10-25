from typing import Protocol
from dataclasses import dataclass

from blitzcrank.domain.Position import Position


@dataclass
class Event:
    type: str
    timestamp: int
    lane_type: str
    monster_type: int
    building_type: str
    original_item: int
    new_item: int

    position: Position
