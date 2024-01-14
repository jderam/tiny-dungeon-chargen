import random
from typing import Any, Dict, List

from tiny_dungeon.data import (
    ADVENTURERS_KIT,
    RACES,
    SAMPLE_WEAPONS,
    TRAITS,
    WEAPON_GROUPS,
)


class TinyDungeonPC:
    """Class to represent a Tiny Dungeons player character."""

    def __init__(self):
        self.race: str = self.random_race()
        self.hp: int = RACES[self.race]["hp"]
        self.race_trait: str = self.get_race_trait()
        self.race_trait_desc: str = self.get_race_trait_desc()
        self.trait1: str = self.add_unique_trait()
        self.trait1_desc: str = TRAITS[self.trait1]
        self.trait2: str = self.add_unique_trait()
        self.trait2_desc: str = TRAITS[self.trait2]
        self.trait3: str = self.add_unique_trait()
        self.trait3_desc: str = TRAITS[self.trait3]
        self.weapon_proficiency: str = random.choice(WEAPON_GROUPS)
        self.weapon: str = random.choice(SAMPLE_WEAPONS[self.weapon_proficiency])
        self.gold_pieces: int = 10
        self.equipment: List[str] = ADVENTURERS_KIT
        self.family_trade: str = ""

    def random_race(self) -> str:
        return random.choice(list(RACES.keys()))

    def get_race_trait(self) -> str:
        if self.race == "Human":
            race_trait = self.random_trait()
        else:
            race_trait = RACES[self.race]["trait"]
        return race_trait

    def random_trait(self) -> str:
        return random.choice(list(TRAITS.keys()))

    def get_race_trait_desc(self) -> str:
        if self.race == "Human":
            race_trait_desc = TRAITS[self.race_trait]
        else:
            race_trait_desc = RACES[self.race]["trait_desc"]
        return race_trait_desc

    def add_unique_trait(self) -> None:
        def _get_trait(key: str) -> str:
            trait = self.as_dict().get(key)
            return trait

        trait_keys = [
            "race_trait",
            "trait1",
            "trait2",
            "trait3",
        ]
        existing_traits = [
            _get_trait(key) for key in trait_keys if _get_trait(key) is not None
        ]
        selectable_traits = [
            trait for trait in TRAITS.keys() if trait not in existing_traits
        ]
        return random.choice(selectable_traits)

    def as_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def print_char(self):
        print()
        print()
        print("NAME: _________________________________")
        print()
        print(f"RACE: {self.race}")
        print()
        print(f"HIT POINTS: {self.hp}")
        print()
        print(f"WEAPON PROFICIENCY: {self.weapon_proficiency}")
        print()
        print(f"WEAPON: {self.weapon}")
        print()
        print("MASTERED WEAPON: ______________________")
        print()
        print("TRAITS")
        print("------------")
        print(f"{self.race_trait}: {self.race_trait_desc}")
        print(f"{self.trait1}: {self.trait1_desc}")
        print(f"{self.trait2}: {self.trait2_desc}")
        print(f"{self.trait3}: {self.trait3_desc}")
        print()
        print("EQUIPMENT")
        print("------------")
        for item in self.equipment:
            print(item)
        print()
        print(f"GOLD PIECES: {self.gold_pieces}")
        print()


if __name__ == "__main__":
    pc = TinyDungeonPC()
    pc.print_char()
