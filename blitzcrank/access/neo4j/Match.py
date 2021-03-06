from dataclasses import dataclass

from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.access.neo4j.Team import TeamNode
from blitzcrank.domain.Match import Match


@dataclass
class MatchNode(Match, GraphObject):
    __primarykey__ = "match_id"
    __primarylabel__ = "MATCH"

    match_id = Property()
    creation_date = Property()
    duration = Property()
    game_type = Property()
    mode = Property()
    queue_id = Property()
    season_id = Property()
    version = Property()
    team = RelatedTo(TeamNode, "HAS_A")
