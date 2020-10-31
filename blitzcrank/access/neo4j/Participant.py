from dataclasses import dataclass

from py2neo.ogm import GraphObject, RelatedTo, Property, Label

from blitzcrank.access.neo4j.Champion import ChampionNode
from blitzcrank.access.neo4j.Event import EventNode
from blitzcrank.access.neo4j.Item import ItemNode
from blitzcrank.access.neo4j.Position import PositionNode
from blitzcrank.domain.Participant import Participant
from blitzcrank.domain.TimeFrame import ParticipantTimeFrame


@dataclass
class TimeFrameNode(ParticipantTimeFrame, GraphObject):
    __primarykey__ = "timeframe_id"
    __primarylabel__ = "TIMEFRAME"
    
    gold_earned = Property()
    level = Property()
    current_gold = Property()
    minions_killed = Property()
    xp = Property()
    position = RelatedTo(PositionNode, "AT")
    events = RelatedTo(EventNode, "OCCURRED")

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ParticipantNode(Participant, GraphObject):
    __primarykey__ = 'participant_id'

    participant_id = Property()
    riot_participant_id = Property()

    items = RelatedTo(ItemNode, "BOUGHT")
    champion = RelatedTo(ChampionNode, "PLAYED")
    champion_level = Property()
    role = Property()
    time_frames = RelatedTo("ParticipantTimeFrame", "HAS_A")

    double_kills = Property()
    triple_kills = Property()
    quadra_kills = Property()
    penta_kills = Property()
    killing_sprees = Property()
    largest_multi_kill = Property()
    largest_killing_spree = Property()
    inhibitor_kills = Property()
    wards_killed = Property()
    unreal_kills = Property()
    deaths = Property()
    turret_kills = Property()
    kills = Property()

    enemy_jungle_minions_killed = Property()
    total_minions_killed = Property()
    neutral_minions_killed = Property()
    team_jungle_minions_killed = Property()

    physical_dmg_dealt_to_champions = Property()
    total_dmg_dealt_to_champions = Property()
    true_dmg_dealt_to_champions = Property()
    dmg_self_mitigated = Property()
    dmg_dealt_to_turrets = Property()
    magic_dmg_dealt_to_champions = Property()
    magic_dmg_taken = Property()
    total_dmg_taken = Property()
    total_physical_dmg_dealt = Property()
    total_magic_dmg_deal = Property()
    true_dmg_taken = Property()
    total_time_cc_dealt = Property()
    true_dmg_dealt = Property()
    total_dmg_dealt = Property()
    largest_crit = Property()
    physical_dmg_taken = Property()
    dmg_dealt_to_objectives = Property()

    perk_primary_style = Property()
    perk_sub_style = Property()
    stat_perk_0 = Property()
    stat_perk_1 = Property()

    sight_wards_bought_in_game = Property()
    vision_wards_bought_in_game = Property()
    time_ccing_others = Property()
    wards_placed = Property()

    killed_first_inhibitor: bool
    assisted_first_tower: bool
    killed_first_tower: bool
    assisted_first_inhibitor: bool
    first_blood_kill: bool
    first_blood_assist: bool

    total_healed = Property()
    total_units_healed = Property()

    longest_living_streak = Property()
    player_score = Property()
    combat_score = Property()
    vision_score = Property()

    gold_earned = Property()
    gold_spent = Property()

    win: Label() # TODO: maybe move this to the relationship between participant and match, plus let it be a Label?

    def __init__(self, participant_id: int):
        self.participant_id = participant_id