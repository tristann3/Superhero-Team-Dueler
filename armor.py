import random
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        '''Return a random block from 0 to the max block the hero can do'''
        random_value = random.randint(0, self.max_block)
        return random_value



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Armor("Debugging Armor", 20)
    print(ability.name)
    print(ability.block())