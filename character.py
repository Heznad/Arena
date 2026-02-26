from database import create_table, add_character
import random
import narrator

class Character:
    def __init__(self, name, hp, attack, armor, dodge, crit, initiative):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.dodge = dodge
        self.crit = crit
        self.add_initiative = initiative
        self.initiative = initiative

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        dmg = dmg * (100 - self.armor) / 100
        dmg = int(dmg)
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return dmg

    def attack_enemy(self, enemy):
        if random.randint(1, 100) <= enemy.dodge:
            narrator.Dodge(self, enemy)
            return

        base = random.randint(int(self.attack - self.attack*0.1), int(self.attack + self.attack*0.1))

        if random.randint(1, 100) <= self.crit:
            mult = random.randint(100, 200) / 100
            base = int(base * mult)
            narrator.Crit(self,enemy)

        dealt = enemy.take_damage(base)
        narrator.Attack(self, dealt, enemy)

    def info(self):
        narrator.Health(self)

def Create_Hero():
    name = input("Введит имя персонажа: ")
    hp = input("Введите количество здоровья: ")
    attack = input("Введите урон от атакаи персонажа: ")
    armor = input("Введите количество защиты персонажа: ")
    dodge = input("Введите вероятность уклонения персонажа: ")
    crit = input("Введите шанс критического урона: ")
    initiative = input("Введите значение инициативы: ")

    hero = Character(
        name= name,
        hp=hp,
        attack=attack,
        armor=armor,
        dodge=dodge,
        crit=crit,
        initiative = initiative
    )   

    create_table()
    add_character(hero)


