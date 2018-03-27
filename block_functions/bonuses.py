class Bonus:
    def __init__(self, source=None, modifies=None, amount=None, duration=None, bonus_type=None, stackable=False):
        self.source = source
        self.modifies = modifies
        self.amount = amount
        self.duration = duration
        self.bonus_type = bonus_type
        self.stackable = stackable


class Racial(Bonus):
    ...


class Dodge(Bonus):
    ...


class Untyped(Bonus):
    ...
