from ability import Ability
from random import randint
class Weapon(Ability):
    def attack(self):
        return randint(self.max_damage//2,self.max_damage)