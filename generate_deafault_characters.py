from character import Character
from database import create_table, add_character

def create_deault_characters():

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

    gladiator4 = Character(
        name="Бронзовый гладиатор 4",
        hp=120,
        attack=11,
        armor=35,
        dodge=8,
        crit=15,
        initiative = 10
    )

    assassin4 = Character(
        name="Пустынный ассасин 4",
        hp=90,
        attack=14,
        armor=15,
        dodge=25,
        crit=30,
        initiative = 15
    )

    gladiator5 = Character(
        name="Бронзовый гладиатор 5",
        hp=120,
        attack=11,
        armor=35,
        dodge=8,
        crit=15,
        initiative = 10
    )

    assassin5 = Character(
        name="Пустынный ассасин 5",
        hp=90,
        attack=14,
        armor=15,
        dodge=25,
        crit=30,
        initiative = 15
    )

    create_table()

    add_character(gladiator1)
    add_character(assassin1)
    add_character(gladiator2)
    add_character(assassin2)
    add_character(gladiator3)
    add_character(assassin3)
    add_character(gladiator4)
    add_character(assassin4)
    add_character(gladiator5)
    add_character(assassin5)


