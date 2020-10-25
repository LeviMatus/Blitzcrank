from typing import Protocol
from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int