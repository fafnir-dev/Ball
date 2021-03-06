"""
Создать класс персонаж +
Свойсва Персонаж: ИД, номер команды +

Создать класс Герой наследник от класа Персонаж +
Свойства Героя: возможность повышать свой уровень +

Создать класс Солдат наследник от класса Персонаж +
Свойства Солдата: следовать за героем своей команды

В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, поднимается уровень.

Отправьте одного из солдат первого героя следовать за ним.
Выведите на экран идентификационные номера этих двух юнитов.
"""

import random  # генератор рандома


class Person:
    # инит списков
    army = []
    good_army = []
    bad_army = []
    heroes = []

    def __init__(self, team):  # инит основнового класса с рандомом ИД и команды
        self.id = id(self)
        self.team = team

    def info_person(self):  # вывод описания перосонажа в зависимости от класса
        if self.__class__.__name__ == 'Hero':
            return self.id, self.team, self.name, self.level
        else:
            return self.id, self.team


class Hero(Person):
    def __init__(self, name, team, level=0):  # инит класса герой
        Person.__init__(self, team)
        self.id = id(self)
        self.name = name
        self.level = level

    def level_up(self):  # инит левел апа
        self.level += 1
        return self.level


class Solider(Person):  # Инит класс солдата
    def follow(self):  # инит следовать за героем
        return "Солдат команды {} c ID:{} следует за героем с ИД: ".format(self.team, self.id)


# инит героев
Person.heroes = [
    Hero("Gedalf", "good"),
    Hero("Sauron", "bad"), ]

for i in range(1, 101):
    Person.army.append(Solider(random.choice(['good', 'bad'])))

for i in Person.army:
    if i.team == 'good':
        Person.good_army.append(i)
    else:
        Person.bad_army.append(i)

if len(Person.good_army) > len(Person.bad_army):
    Person.heroes[0].level_up()
    print(f"Герой:{Person.heroes[0].name} с ИД{Person.heroes[1].id}, Уровень: {Person.heroes[0].level}")
    print(f"Размер армии: {len(Person.good_army)}")
    print(f"Войска на поле боя: {len(Person.army)}")
elif len(Person.good_army) < len(Person.bad_army):
    Person.heroes[1].level_up()
    print(f"Герой:{Person.heroes[1].name} с ИД{Person.heroes[1].id}, Уровень: {Person.heroes[1].level}")
    print(f"Размер армии: {len(Person.bad_army)}")
    print(f"Войска на поле боя: {len(Person.army)}")
else:
    print("Армии равны")
    print(f"Войска на поле боя: {len(Person.army)}")

print(Person.heroes[0].id)
print(Person.heroes[1].id)
print(Solider.army[0].follow())
