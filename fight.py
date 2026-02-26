from team import Team
from character import Character
import random

class Fight:

    def __init__(self, team_1, team_2):
        self.team_1 = team_1
        self.team_2 = team_2


    def fight(self):

        acting_characters = []

        for c in self.team_1.characters:
            if c.is_alive():
                if c.initiative > 100:
                    acting_characters.append(c)
                else:
                    c.initiative += c.add_initiative
        for c in self.team_2.characters:
            if c.is_alive():
                if c.initiative > 100:
                    acting_characters.append(c)
                else:
                    c.initiative += c.add_initiative

        p = random.randint(0, 100)
        if not len(acting_characters) == 0:
            hero = acting_characters[random.randint(0, len(acting_characters)-1)]
            if "гладиатор" in hero.name:
                enemy = self.team_2.characters[random.randint(0, len(self.team_2.characters)-1)]
                hero.attack_enemy(enemy)
                hero.initiative = 0
            else:
                enemy = self.team_1.characters[random.randint(0, len(self.team_1.characters)-1)]
                hero.attack_enemy(enemy)
                hero.initiative = 0


        