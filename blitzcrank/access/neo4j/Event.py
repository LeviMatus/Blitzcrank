from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.access.neo4j.Position import PositionNode
from blitzcrank.domain.Event import Event


class EventNode(Event, GraphObject):
    event_type = Property()
    timestamp = Property()
    lane_type = Property()
    monster_type = Property()
    building_type = Property()
    original_item = Property()
    new_item = Property()
    position = RelatedTo(PositionNode, "AT")
    __primarylabel__ = 'EVENT'

    def __init__(self, type, timestamp, lane, monster, building=None, original_item=None, new_item=None, position=None):
        self.__dict__.update(kwargs)
