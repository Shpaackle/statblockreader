from enum import Enum


class Bonus:
    """
    Represents basic bonus class
    """
    def __init__(
            self,
            bonus_type=None,
            name=None,
            source=None,
            modifies=None,
            amount=-999,
            active=False,
            stackable=False,
            duration=None,
            penalty=False,
    ):
        self.bonus_type = bonus_type
        self.name = name
        self.source = source
        self.modifies = modifies
        self.amount = amount
        self.duration = duration
        self.stackable = stackable
        self.penalty = penalty or (amount <= 0)
        self.active = active
        self.conditions = []

    def change_active_state(self):
        self.active = not self.active


class BaseAttackBonus(Bonus):
    # TODO: Move this to attributes.py
    def __init__(self):
        super(BaseAttackBonus, self).__init__(source="Base Attack Bonus")


class RacialBonus(Bonus):
    def __init__(self, source=None):
        super(RacialBonus, self).__init__(bonus_type="Racial", source=source)


class DodgeBonus(Bonus):
    def __init__(self, source=None):
        super(DodgeBonus, self).__init__(bonus_type="Dodge", source=source, stackable=True)


class UntypedBonus(Bonus):
    def __init__(self, source=None):
        super(UntypedBonus, self).__init__(bonus_type="Untyped", source=source, stackable=True)


class BONUSES(Enum):
    BAB = BaseAttackBonus()
    racial = RacialBonus()
    dodge = DodgeBonus()
    untyped = UntypedBonus()
    EMPTY = Bonus()

    @staticmethod
    def create_bonus(bonus_type="EMPTY", **kwargs):

        bonus = BONUSES[bonus_type].value

        for k, v in kwargs.items():
            bonus.__setattr__(k, v)


        return bonus
