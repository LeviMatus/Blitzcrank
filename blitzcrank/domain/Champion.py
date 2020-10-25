from typing import Protocol
from dataclasses import dataclass


@dataclass
class Champion:
    champion_id: str
    name: str
    title: str
