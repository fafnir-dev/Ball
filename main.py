import random


class Person():
    def __init__(self, name, surname, qual=1):
        self.name = name
        self.surname = surname
        self.qual = qual

    def print_person(self):
        print(f"Name: {self.name} Surname: {self.surname} Quality: {self.qual}")

    def fired_person(self):
        print(f"Goodbay {self.name} {self.surname}")


p = [
     Person("Bob", "Marley", random.randint(1, 11)),
     Person("Don", "Baron", random.randint(1, 11)),
     Person("Donald", "Dack", random.randint(1, 11))
    ]

fired = sorted(p, key=lambda Person: Person.qual, reverse=True)

for i in fired:
    i.print_person()

fired[-1].fired_person()
