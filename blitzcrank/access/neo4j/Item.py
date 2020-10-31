from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.domain.Item import Item


class ItemNode(Item, GraphObject):
    item_id = Property()
    name = Property()
    cost = Property()
    description = Property()
    base_cost = Property()
    sells_for = Property()

    builds = RelatedTo("ITEM", "BUILDS")
    __primarylabel__ = 'ITEM'
    __primarykey__ = "item_id"

    def __init__(self, item_id: int, name: str, cost: int, description: str, base_cost: int, sells_for: int, builds=None):
        self.item_id = item_id
        self.name = name
        self.cost = cost
        self.description = description
        self.base_cost = base_cost
        self.sells_for = self
        self.builds = builds
