from py2neo.ogm import GraphObject, Property

from blitzcrank.domain.Champion import Champion


class ChampionNode(Champion, GraphObject):
    champion_id = Property()
    name = Property()
    __primarykey__ = 'champion_id'
    __primarylabel__ = 'CHAMPION'

