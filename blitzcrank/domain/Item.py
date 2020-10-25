from typing import Protocol
from dataclasses import dataclass


@dataclass
class Item:
    item_id: int
    name: str
    cost: int
    description: str
    base_cost: int
    sells_for: int
