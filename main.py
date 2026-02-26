from character import Character, Create_Hero
from database import get_all_characters
from generate_deafault_characters import create_deault_characters
from team import Team
from fight import Fight
import narrator
import random
import time

comand = 10

while comand != 0:
    narrator.HelloWorld()
    print("1. Бой 1 на 1\n"+
          "2. Бой 3 а 3\n"+
          "3. Создание персонажа\n"+
          "0. Выход")
    comand = input("Введите команду: ")
    if comand == '1':
        pull_heroes = get_all_characters()
        if len(pull_heroes) >= 2:
            list_heroes = []
            for _ in pull_heroes:
                
                hero = Character(
                    name=_[1],
                    hp=_[2],
                    attack=_[3],
                    armor=_[4],
                    dodge=_[5],
                    crit=_[6],
                    initiative=_[7]
                )
                list_heroes.append(hero)

            i = 1
            for hero in list_heroes:
                print(i)
                print(hero.name, hero.)
        else:
            print("Не хватает героев для боя!")
    elif comand == '2':
        pull_heroes = get_all_characters()
        print(pull_heroes)
    elif comand == '3':
        Create_Hero()
    elif comand == '0':
        exit()
    else:
        print("Введена некорректная команда")


gladiator1 = Character(
    name="Бронзовый гладиатор 1",
    hp=120,
    attack=11,
    armor=35,
    dodge=8,
    crit=15,
    initiative = 10
)

assassin1 = Character(
    name="Пустынный ассасин 1",
    hp=90,
    attack=14,
    armor=15,
    dodge=25,
    crit=30,
    initiative = 15
)

gladiator2 = Character(
    name="Бронзовый гладиатор 2",
    hp=120,
    attack=11,
    armor=35,
    dodge=8,
    crit=15,
    initiative = 10
)

assassin2 = Character(
    name="Пустынный ассасин 2",
    hp=90,
    attack=14,
    armor=15,
    dodge=25,
    crit=30,
    initiative = 15
)

gladiator3 = Character(
    name="Бронзовый гладиатор 3",
    hp=120,
    attack=11,
    armor=35,
    dodge=8,
    crit=15,
    initiative = 10
)

assassin3 = Character(
    name="Пустынный ассасин 3",
    hp=90,
    attack=14,
    armor=15,
    dodge=25,
    crit=30,
    initiative = 15
)

team_Gladiators = Team(
    name="Гладиаторы",
    characters = [gladiator1, gladiator2, gladiator3]
)

team_Assassins = Team(
    name="Ассассины",
    characters = [assassin1, assassin2, assassin3]
)

while not team_Gladiators.is_defeated() and not team_Assassins.is_defeated():
    
    fight = Fight(
        team_1 = team_Gladiators,
        team_2 = team_Assassins
    )
    fight.fight()
    team_Gladiators.info()
    team_Assassins.info()
    time.sleep(1)
    print()
    

if team_Gladiators.is_defeated():
    narrator.EndFight(team_Gladiators.name)
else:
    narrator.EndFight(team_Assassins.name)