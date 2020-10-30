from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedObjects

from blitzcrank.access.neo4j.Incarnation import IncarnationNode
from blitzcrank.domain.Summoner import Summoner


class SummonerNode(Summoner, GraphObject):
    summoner_id = Property()
    account_id = Property()
    puuid: Property()
    incarnations: RelatedObjects = RelatedTo(IncarnationNode, 'HAS')
    __primarykey__ = 'summoner_id'
    __primarylabel__ = 'SUMMONER'
