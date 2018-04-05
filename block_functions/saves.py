from .attributes import Attribute


class Save(Attribute):
    def __init__(self, name):
        super(Save, self).__init__(name=name)
