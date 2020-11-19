from random import randint
from ability import Ability
from armor import Armor

class Hero:

    def __init__ (self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''currently chooses a random winner'''
        num = randint(1,2) #random number, 1 or 2
        if num == 1:
            print("Winner")
        else:
            print("Loser")
    
    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)
    
    def attack(self):
        '''iterates through the abilities list and gets the attack for each ability'''
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack
    def add_armor(self, armor):
        '''Add armor to the list of armors'''
        self.armors.append(armor)
    def defend(self, damage_amt):
        '''iterates through the list of armors list and gets defense for each armor'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''sets the current health to the new value after taking damage'''
        self.current_health = self.current_health - (damage - self.defend(damage))
        pass
    def is_alive(self):
        '''return True or Flase depending on wether or not the hero is alive'''
        if self.current_health <= 0:
            return False
        else:
            return True
        






if __name__ == "__main__":
    #this code block is run if init from terminal
    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
