class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class LightSource(Item):
    def __init__(self, name, description, provides_light):
        Item.__init__(self, name, description)
        self.provides_light: provides_light
