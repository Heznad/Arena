from character import Character
from team import Team
from fight import Fight
import random
import time

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
    print("Победил", team_Gladiators.name)
else:
    print("Победил", team_Assassins.name)