class Person():
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

p = Person("Bob", "Marley")
p1 = Person("Jack", "Daniels")
print(p.name, p.surname)
print(p1.name, p1.surname)
