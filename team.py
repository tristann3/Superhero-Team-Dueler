import random
class Team():
    def __init__(self, name):
        '''Initializes a team name and an empty list of heroes'''
        self.name = name
        self.heroes = list()
    
    def add_hero(self, hero):
        '''Add Hero object to self.heroes'''
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        '''Remove a Hero object from the list of heroes'''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        #if the hero is not found, the flag variable would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints all the heroes to the console'''
        output = ""
        for hero in self.heroes:
            output = output + hero.name + " "
        print(output)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths: {}".format(
                hero.name,kd
            ))
    
    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        '''Battle each team against each other'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            if hero.current_health <= 0:
                living_heroes.remove(hero)
            elif opponent.current_health <= 0:
                living_opponents.remove(opponent)
                                   

            
