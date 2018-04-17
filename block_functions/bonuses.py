class Bonus:
    """
    Represents basic bonus class
    """
    def __init__(
            self,
            name=None,
            source=None,
            modifies=None,
            amount=-999,
            duration=None,
            bonus_type=None,
            stackable=False,
            is_penalty=False,
    ):
        self.name = name
        self.source = source
        self.modifies = modifies
        self.amount = amount
        self.duration = duration
        self.bonus_type = bonus_type
        self.stackable = stackable
        self.is_penalty = is_penalty or (amount <= 0)
        self.active = False

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
