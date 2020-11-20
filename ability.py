import random
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        '''Return a random attack from 0 to the max attack the hero can do'''
        random_value = random.randint(0, self.max_damage)
        return random_value


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.max_damage)