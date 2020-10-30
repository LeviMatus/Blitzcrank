from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.access.neo4j.Participant import PositionNode
from blitzcrank.domain.Event import Event


class ChampionNode(Event, GraphObject):
    event_type = Property()
    timestamp = Property()
    lane_type = Property()
    monster_type = Property()
    building_type = Property()
    original_item = Property()
    new_item = Property()
    position = RelatedTo(PositionNode, "AT")
    __primarylabel__ = 'EVENT'
