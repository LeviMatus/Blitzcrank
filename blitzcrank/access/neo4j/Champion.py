from py2neo.ogm import GraphObject, Property

from blitzcrank.domain.Champion import Champion


class ChampionNode(Champion, GraphObject):
    champion_id = Property()
    name = Property()
    __primarykey__ = 'champion_id'
    __primarylabel__ = 'CHAMPION'

    def __init__(self, champ_id: int, name: str) -> None:
        self.champion_id = champ_id
        self.name = name
