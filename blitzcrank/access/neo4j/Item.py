from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.domain.Item import Item


class ItemNode(Item, GraphObject):
    name = Property()
    cost = Property()
    description = Property()
    base_cost = Property()
    sells_for = Property()

    builds = RelatedTo("ITEM", "BUILDS")
    __primarylabel__ = 'ITEM'
