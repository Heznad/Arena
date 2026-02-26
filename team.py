from character import Character

class Team:

    def __init__(self, name, characters):
        self.name = name
        self.characters = characters

    def is_defeated(self):
        for c in self.characters:
            if c.is_alive():
                return False
        return True

    def info(self):
        print(self.name)
        for c in self.characters:
            c.info()
            print(f"Инициатива: {c.initiative}")

def Create_Team(characters = []):
    name = input("Введите название команды:")
    team = Team(
        name= name,
        characters = characters
    )