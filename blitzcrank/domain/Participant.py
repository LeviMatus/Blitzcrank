from typing import Protocol, List
from dataclasses import dataclass

from blitzcrank.domain.Champion import Champion
from blitzcrank.domain.Incarnation import Incarnation
from blitzcrank.domain.Item import Item
from blitzcrank.domain.TimeFrame import ParticipantTimeFrame


@dataclass
class Participant:
    participant_id: int
    riot_participant_id: int
    incarnation: Incarnation

    items: List[Item]
    champion: Champion
    champion_level: int
    role: str
    time_frames = List[ParticipantTimeFrame]

    double_kills: int
    triple_kills: int
    quadra_kills: int
    penta_kills: int
    killing_sprees: int
    largest_multi_kill: int
    largest_killing_spree: int
    inhibitor_kills: int
    wards_killed: int
    unreal_kills: int
    deaths: int
    turret_kills: int
    kills: int

    enemy_jungle_minions_killed: int
    total_minions_killed: int
    neutral_minions_killed: int
    team_jungle_minions_killed: int

    physical_dmg_dealt_to_champions: int
    total_dmg_dealt_to_champions: int
    true_dmg_dealt_to_champions: int
    dmg_self_mitigated: int
    dmg_dealt_to_turrets: int
    magic_dmg_dealt_to_champions: int
    magic_dmg_taken: int
    total_dmg_taken: int
    total_physical_dmg_dealt: int
    total_magic_dmg_deal: int
    true_dmg_taken: int
    total_time_cc_dealt: int
    true_dmg_dealt: int
    total_dmg_dealt: int
    largest_crit: int
    physical_dmg_taken: int
    dmg_dealt_to_objectives: int

    perk_primary_style: int
    perk_sub_style: int
    stat_perk_0: int
    stat_perk_1: int

    sight_wards_bought_in_game: int
    vision_wards_bought_in_game: int
    time_ccing_others: int
    wards_placed: int

    killed_first_inhibitor: bool
    assisted_first_tower: bool
    killed_first_tower: bool
    assisted_first_inhibitor: bool
    first_blood_kill: bool
    first_blood_assist: bool

    total_healed: int
    total_units_healed: int

    longest_living_streak: int
    player_score: int
    combat_score: int
    vision_score: int

    gold_earned: int
    gold_spent: int

    win: bool


class ParticipantService(Protocol):
    def participant(self, participant_id: int) -> Participant:
        raise NotImplemented

    def create_participant(self, participant: Participant):
        raise NotImplemented
