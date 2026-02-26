def HelloWorld():
    print("Здравствувйте! Вы попали на арену!")

def Dodge(hero, enemy):
    print(enemy.name, " уклонился от аттаки ", hero.name, "!")

def Crit(hero, enemy):
    print(hero.name, f"наносит критический урон {enemy.name}!")

def Attack(hero, dealt, enemy):
    print(f"{hero.name} наносит {dealt} урона {enemy.name}")

def Health(hero):
    print(f"{hero.name} HP: {hero.hp} / {hero.max_hp}")

def EndFight(winner_team):
    print(f"Бой окончен! Победили - {winner_team}")