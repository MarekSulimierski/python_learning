import sqlite3
con = sqlite3.connect('recipeCalc.db')
con.row_factory = sqlite3.Row

cur = con.cursor()

cur.executescript("""
DROP TABLE IF EXISTS danie;
CREATE TABLE IF NOT EXISTS danie (
id INTEGER PRIMARY KEY ASC,
nazwa varchar(50) NOT NULL,
opis varchar(250) NOT NULL,
cena INTEGER NOT NULL)""")

while True:

    print("Rozpocznij dodawanie nowego dania:")
    noweDanie = [None,]

    nazwaDania = input("Podaj nazwę dania: ")
    noweDanie.append(nazwaDania)

    opisDania = input("Podaj krótki opis dania: ")
    noweDanie.append(opisDania)
# Kalkulacja ceny
    cenaDania = input("Wybierz składnik z listy: ")

    cur.execute(
        """
        SELECT  cena FROM skladniki WHERE id = 
        """)

    noweDanie.append(nazwaDania)
