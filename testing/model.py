from mongoengine import *\


class BasicItem(Document):
    """A generic item"""

    name = StringField(max_length=120, required=True)
    category = StringField(max_length=120)
    subcategory = StringField(max_length=120)
    price = StringField(max_length=120)
    weight = StringField(max_length=120)
    description = StringField()
    cost = StringField(max_length=120)
    source = StringField(max_length=120)
    id = IntField()
    material = StringField()
    
    meta = {"allow_inheritance": True}
    
    
class MagicItem(BasicItem):
    aura = StringField(max_length=120)
    slot = StringField(max_length=120)
    requirements = StringField()
    caster_level = StringField(max_length=120)
    bonus = StringField()
    construction = ListField(StringField())
    subtype = StringField(max_length=120)


class Weapon(MagicItem):
    critical = StringField(max_length=120)
    damage = ListField(StringField(max_length=120))
    proficiency = StringField(max_length=120)
    damage_type = StringField(max_length=120, required=True)
    special = ListField(StringField)
    range_increment = IntField()


class Armor(MagicItem):
    arcane_spell_failure = StringField(max_length=120, required=True)
    armor_bonus = StringField(max_length=120)
    armor_type = StringField(max_length=120)
    max_dex_bonus = StringField(max_length=120)
    speed = ListField(StringField(max_length=120))
    shield_bonus = StringField(max_length=120)


class Race(Document):
    name = StringField(max_length=120)
    category = StringField(max_length=120)
    subcategory = StringField(max_length=120)


class Feat(Document):
    name = StringField(max_length=120)
    category = StringField(max_length=120)
    description = StringField()
    prerequisites = ListField(StringField())
    prerequisite_feats = ListField(StringField())
    benefit = StringField()
    normal = StringField()
    source = StringField(max_length=120)
    multiples = BooleanField()


class Spell(Document):
    name = StringField()
    school = StringField()
    subschool = StringField()
    descriptor = StringField()
    spell_level = ListField(StringField(max_length=120))
    casting_time = StringField()
    components = StringField()
    costly_component = BooleanField()
    _range = StringField()
    area = StringField()
    effect = StringField()
    targets = StringField()
    duration = StringField()
    dismissible = BooleanField()
    shapeable = BooleanField()
    saving_throw = StringField()
    spell_resistance = StringField()
    description = StringField()
    source = StringField()


class Scroll(MagicItem):
    is_arcane = BooleanField()
    is_divine = BooleanField()
    spell = ReferenceField(Spell)


class Wand(MagicItem):
    charges = IntField()
    spell = ReferenceField(Spell)


class Skill(Document):
    name = StringField(max_length=120)
    ability = StringField(max_length=120)
    untrained = BooleanField()
    armor_check = BooleanField()
    subtype = BooleanField()


class _Class(Document):
    name = StringField(max_length=120)
    skills = ListField(StringField(max_length=120))
    saves = ListField(StringField(max_length=120))
    hit_die = StringField(max_length=120)
    BAB = StringField(max_length=120)
    abilities = ListField(StringField)
