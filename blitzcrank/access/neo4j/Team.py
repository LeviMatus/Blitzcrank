from dataclasses import dataclass

from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.access.neo4j.Participant import ParticipantNode
from blitzcrank.domain.Team import Team


@dataclass
class TeamNode(Team, GraphObject):
    __primarykey__ = "team_id"
    __primarylabel__ = "TEAM"

    team_id = Property()
    color = Property()
    participants = RelatedTo(ParticipantNode, "HAS_A")

    def __init__(self, id: int, color: str) -> None:
        self.team_id = id
        self.color = color
