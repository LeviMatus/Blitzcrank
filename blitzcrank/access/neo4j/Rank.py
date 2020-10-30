from py2neo.ogm import GraphObject, Property

from blitzcrank.domain.Rank import Rank


class RankNode(Rank, GraphObject):
    rank = Property()
    tier = Property()
    division = Property()
    queue = Property()
    __primarykey__ = "rank"
    __primarylabel__ = "RANK"

    def __init__(self, tier, division, queue):
        self.tier = tier
        self.queue = queue
        self.division = division
        self.rank = '{}-{}-{}'.format(queue, tier, division)