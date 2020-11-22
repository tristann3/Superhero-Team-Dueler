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