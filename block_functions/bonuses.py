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

    def change_active(self):
        self.active = not self.active

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.amount} {self.modifies})"


class BaseAttackBonus(Bonus):
    # TODO: Move this to attributes.
    def __init__(self):
        super(BaseAttackBonus, self).__init__(source="Base Attack Bonus")


class RacialBonus(Bonus):
    def __init__(self, source=None, **kwargs):
        super(RacialBonus, self).__init__(bonus_type="Racial",
                                          source=source,
                                          **kwargs, )


class DodgeBonus(Bonus):
    def __init__(self, source=None, **kwargs):
        super(DodgeBonus, self).__init__(bonus_type="Dodge",
                                         source=source,
                                         stackable=True,
                                         **kwargs, )


class UntypedBonus(Bonus):
    def __init__(self, source=None, **kwargs):
        super(UntypedBonus, self).__init__(bonus_type="Untyped",
                                           source=source,
                                           stackable=True,
                                           **kwargs, )


class CompetenceBonus(Bonus):
    def __init__(self, source=None, **kwargs):
        super(CompetenceBonus, self).__init__(bonus_type="Competence",
                                              source=source,
                                              stackable=False,
                                              **kwargs, )


class SacredBonus(Bonus):
    def __init__(self, source=None, **kwargs):
        super(SacredBonus, self).__init__(bonus_type="Sacred",
                                          source=source,
                                          stackable=False,
                                          **kwargs, )


class BONUSES(Enum):
    BAB = BaseAttackBonus
    racial = RacialBonus
    dodge = DodgeBonus
    untyped = UntypedBonus
    competence = CompetenceBonus
    sacred = SacredBonus
    EMPTY = Bonus

    @staticmethod
    def create_bonus(bonus_type="EMPTY", **kwargs):
        return BONUSES[bonus_type].value(**kwargs)
