from enum import Enum


class Bonus:
    def __init__(self, source=None, modifies=None, amount=None, duration=None, bonus_type=None, stackable=False,
                 penalty=False):
        self.source = source
        self.modifies = modifies
        self.amount = amount
        self.duration = duration
        self.bonus_type = bonus_type
        self.stackable = stackable
        self.penalty = penalty


class BaseAttackBonus(Bonus):
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


class Bonuses(Enum):
    BAB = BaseAttackBonus()
    Racial = RacialBonus()
    Dodge = DodgeBonus()
    Untyped = UntypedBonus()
    EMPTY = Bonus()

    @staticmethod
    def create_bonus(bonus_type=None, **kwargs):
        if not bonus_type:
            return Bonuses.EMPTY
        else:
            bonus = bonus_type

        for k, v in kwargs.items():
            bonus.k = v

        return bonus
