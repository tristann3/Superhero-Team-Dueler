from random import randint

class Hero:
    def __init__ (self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    def fight(self, opponent):
        num = randint(1,2)
        if num == 1:
            print("Winner")
        else:
            print("Loser")



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    opponent = Hero("GraceHOOPER", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    my_hero.fight(opponent)