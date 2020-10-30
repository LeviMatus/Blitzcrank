from py2neo.ogm import GraphObject, Property, RelatedTo

from blitzcrank.access.neo4j.Participant import ParticipantNode
from blitzcrank.domain.Team import Team


class TeamNode(Team, GraphObject):
    __primarykey__ = "team_id"
    __primarylabel__ = "TEAM"

    color = Property()
    participants = RelatedTo(ParticipantNode, "HAS_A")