import random

NAMES_F = ['Yolanda', 'Nashri', 'Ala', 'Gotha']
NAMES_M = ['Alarich', 'Hunnerich', 'Athaulf', 'Theoderich']

class person:
    #sex
    #age
    #mother
    #father
    #isAlive

    # a person is born. This is how one 
    # should create a person.
    def init(mother, father):
        self.mother = mother #TODO check mother, father are person objs
        self.father = father
        self.age = 0
        self.isAlive = 1
        self.sex = random.choice(['m', 'f'])
        if sex == 'f':
            self.name = random.choice(NAMES_F) + ', daughter of ' + self.father
        else:
            self.name = random.choice(NAMES_M) + ', son of ' + self.father

    def age(self):
        self.age += 1
        if age > 60: #TODO use a probability function
            # die
            isAlive = 0
