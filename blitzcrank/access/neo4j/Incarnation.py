from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedObjects

from blitzcrank.domain.Incarnation import Incarnation
from blitzcrank.access.neo4j.Rank import RankNode


class IncarnationNode(Incarnation, GraphObject):
    summoner_name = Property()
    ranks: RelatedObjects = RelatedTo(RankNode, 'RANKED')
    __primarykey__ = 'summoner_name'
    __primarylabel__ = 'INCARNATION'

    def __init__(self, name):
        self.summoner_name = name
