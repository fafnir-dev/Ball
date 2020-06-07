import random


class Person:
    id_persons = 0
    team_name = ['good', 'bad']

    def __init__(self, team):
        self.id = Person.id_persons
        self.team = team
        Person.id_persons += 1

    def infoPerson(self):
        if self.__class__.__name__ == 'Hero':
            print(self.__class__.__name__, Hero.id_persons, self.team, self.level)
        else:
            print(self.__class__.__name__, self.id_persons, self.team)


class Hero(Person):
    def __init__(self, team, name):
        Person.__init__(self, team)
        self.name = name
        self.level = 1

    def levelUp(self):
        self.level += 1


class Solider(Person):
    def __init__(self, team: object) -> object:
        Person.__init__(self, team)
        self.team = team


    def goToHero(self):
        if self.team == 'good':
            print(f"ID {self.id} team {self.team} Set {gendalf.name} hero {gendalf.id}")
        else:
            print(f"ID {self.id} team {self.team} Set {sauron.name} hero {sauron.id}")


gendalf = Hero('good', 'Gendalf')
sauron = Hero('bad', 'Sauron')
army = []
for i in range(int(input("Enter len army:\n"))):
    army.append(Solider(random.choice(Person.team_name)))

a = int(input("Who is:\n"))
army[a].goToHero()

for i in army:
    good =[]
    bad = []
    if i.team == 'good':
        good.append(i)
    else: bad.append(i)

g = len(good)
b = len(bad)
if g > b:
    print("Good team WIN")
elif g < b:
    print ("Bad team WIN")
else: print("No WIN")