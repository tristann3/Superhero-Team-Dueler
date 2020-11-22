from random import randint
from ability import Ability
from weapon import Weapon
from armor import Armor

class Hero:

    def __init__ (self, name, starting_health=100):
        self.abilities = list() #holds weapons and abilities
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        '''currently chooses a random winner'''
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return
        while self.is_alive() and opponent.is_alive():
            attack = self.attack()
            opponent.take_damage(attack)

            attack = opponent.attack()
            self.take_damage(attack)
        else:
            if self.is_alive():
                print(f"{self.name} Won!")
            else:
                print(f"{opponent.name} Won!")
            
    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)
    def add_weapon(self, weapon):
        '''Add weapon to weapons list'''
        self.abilities.append(weapon)
    
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
        
        return damage_amt - total_block

    def take_damage(self, damage):
        '''sets the current health to the new value after taking damage'''
        self.current_health = self.current_health - self.defend(damage)
        pass
    def is_alive(self):
        '''return True or Flase depending on wether or not the hero is alive'''
        if self.current_health <= 0:
            return False
        else:
            return True
        






if __name__ == "__main__":
    #this code block is run if init from terminal
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())




