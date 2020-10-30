from py2neo.ogm import GraphObject, Property


class Position(GraphObject):
    __primarykey__ = 'position_id'

    position_id = Property()
    x = Property()
    y = Property()

    def __init__(self, x, y):
        self.position_id = str(x) + "-" + str(y)
        self.x = x
        self.y = y
