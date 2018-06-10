import math
from collections import defaultdict
from typing import Dict


def from_db(category: str, name: str) -> Dict:
    # TODO: add call to database
    ...


class Bonuses(list):
    @property
    def total(self):
        return 0


class _Race:
    def __init__(self, db_race: dict, ):
        self.db = db_race
        self.traits = db_race.get("traits", list())
        self.bonuses = defaultdict(list)


class _Attribute:
    def __init__(self,
                 name: str,
                 _block: str = "-999",
                 base: int = 10, ):
        self.name = name
        self.unmodified = base
        self.block = int(_block)
        self.bonuses = Bonuses([0])

    def __call__(self):
        raise NotImplementedError()


class _AbilityScore(_Attribute):
    def __init__(self,
                 name: str,
                 _block: str = "-999",
                 base: int = 10, ):
        super(_AbilityScore, self).__init__(name=name, base=base, _block=_block)
        self.total = self()

    def __call__(self):
        return self.unmodified + self.bonuses.total

    @property
    def mod(self) -> int:
        return int(math.floor((self() - 10) / 2))

    def __repr__(self):
        return f"({self.__class__.__name__}){self.name}: {self.total} [{self.mod}]"


class _ArmorClass(_Attribute):
    def __init__(self, _block: str = "10"):
        super(_ArmorClass, self).__init__(name="Armor Class")

    def __call__(self):
        return self.unmodified + self.bonuses.total


class _Character:
    def __init__(self, block: Dict[str, str], ):
        self.block = block
        self.name = block["name"]
        self.race = block["race"]
        self.alignment = block["alignment"]
        self.size = block["size"]
        self.CR = block["cr"]
        self.age = block.get("age", "")
        self.gender = block.get("gender", "")
        self.XP = block["xp"]
        self.classes = {"block": block["classes"]}
        """
        # TODO: add abilities from block
        # Ability Scores
        """
        self.STR = _AbilityScore("Strength", _block=block["STR"])
        self.DEX = _AbilityScore("Dexterity", _block=block["DEX"])
        self.CON = _AbilityScore("Constitution", _block=block["CON"])
        self.INT = _AbilityScore("Intelligence", _block=block["INT"])
        self.WIS = _AbilityScore("Wisdom", _block=block["WIS"])
        self.CHA = _AbilityScore("Charisma", _block=block["CHA"])
        self.AC = _ArmorClass(_block=block["AC"])
        self.HP = ""
        self.FORT = ""
        self.REF = ""
        self.WILL = ""
        self.speed = ""
