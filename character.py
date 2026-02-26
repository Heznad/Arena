import random

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
            print(enemy.name, "уклонился!")
            return

        base = random.randint(int(self.attack - self.attack*0.1), int(self.attack + self.attack*0.1))

        if random.randint(1, 100) <= self.crit:
            mult = random.randint(100, 200) / 100
            base = int(base * mult)
            print(self.name, "наносит крит!")

        dealt = enemy.take_damage(base)
        print(self.name, "наносит", dealt, "урона", enemy.name)



    def info(self):
        print(self.name, "HP:", self.hp, "/", self.max_hp)



