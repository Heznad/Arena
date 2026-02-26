import sqlite3

connection = sqlite3.connect("arena_database.db")
cursor = connection.cursor()
connection.close()

def create_table():
    with sqlite3.connect("arena_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            hp INTEGER,
            attack INTEGER,
            armor INTEGER,
            dodge INTEGER,
            crit INTEGER,
            initiative INTEGER
        )
        """)

def add_character(character):
    with sqlite3.connect("arena_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO characters (name, hp, attack, armor, dodge, crit, initiative)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            character.name,
            character.hp,
            character.attack,
            character.armor,
            character.dodge,
            character.crit,
            character.initiative
        ))

def get_all_characters():
    with sqlite3.connect("arena_database.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM characters")
        return cursor.fetchall()

