from mongoengine import *\


class Basic_Item(Document):
    """A generic item"""
    
    name = StringField(max_length=120, required=True)
    category = StringField(max_length=120)
    price = StringField(max_length=120)
    weight = StringField(max_length=120)
    description = StringField()
    cost = StringField(max_length=120)
    source = StringField(max_length=120)
    id = IntField()
    
    meta = {"allow_inheritance": True}
    
    
class Magic_Item(Basic_Item):
	slot = StringField(max_length=120)
	requirements = StringField()
	caster_level = StringField(max_length=120)
	bonus = 
