from dataclasses import dataclass

from blitzcrank.domain.Event import Event
from blitzcrank.domain.Position import Position


@dataclass
class ParticipantTimeFrame:
    frame_id: int
    gold_earned: int
    level: int
    current_gold: int
    minions_killed: int
    xp: int
    position: Position
    events: Event
