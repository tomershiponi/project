import random
from classes.game import *


class Spell:

    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type



    def __str__(self):
        return f"{self.name}\n{self.cost}\n{self.dmg}"

    def get_spell_name(self, i):
        return self.name

    def get_spell_mp_cost(self, i):
        return self.cost

    def generatre_spall_dmg(self):
        mgl = self.dmg - 5
        mgh = self.dmg + 5
        return random.randrange(mgl, mgh)







