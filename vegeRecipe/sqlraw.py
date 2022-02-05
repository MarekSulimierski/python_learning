import sqlite3
con = sqlite3.connect('recipeCalc.db')
con.row_factory = sqlite3.Row

cur = con.cursor()

#cur.execute("DROP TABLE IF EXISTS skladniki;")

#cur.execute("""
#   CREATE TABLE IF NOT EXISTS skladniki (
#      id INTEGER PRIMARY KEY ASC,
#        nazwa varchar(250) NOT NULL,
#        jedMiary varchar(10) DEFAULT 'kg',
#        cena FLOAT NOT NULL
 #   )""")

# cur.executescript("""
#    DROP TABLE IF EXISTS danie;
#    CREATE TABLE IF NOT EXISTS danie (
#       id INTEGER PRIMARY KEY ASC,
#        nazwa varchar(50) NOT NULL,
#        opis varchar(250) NOT NULL,
#        cena INTEGER NOT NULL)""")

#cur.execute('INSERT INTO skladniki VALUES(NULL, ?, ?, ?);', ('pieprz', 'kg', 70.00))
#cur.execute('INSERT INTO skladniki VALUES(NULL, ?, ?, ?);', ('oregano', 'kg', 175.00))

while True:

    print("Rozpocznij dodawanie nowego składnika:")
    nowySkladnik = [None,]

    nazwaSkladnika = input("Podaj nazwę składnika: ")
    nowySkladnik.append(nazwaSkladnika)

    jedMiarySkladnika = input("Podaj jednostkę miary: ")
    nowySkladnik.append(jedMiarySkladnika)

    cenaSkladnika = input("Podaj cenę składnika: ")
    nowySkladnik.append(cenaSkladnika)

    nowySkladnik = tuple(nowySkladnik)

    cur.execute('INSERT INTO skladniki VALUES(?, ?, ?, ?);', nowySkladnik)

    addOrNotAdd = input("Czy chcesz dodać nowy składnik T/N")
    if addOrNotAdd == "T":
        continue
    if addOrNotAdd == "N":
        break


    con.commit()


def czytajdane():

    cur.execute(
        """
        SELECT id, nazwa, jedMiary, cena FROM skladniki
        """)
    listaSkladnikow = cur.fetchall()
    for skladniki in listaSkladnikow:
        print(skladniki['id'], skladniki['nazwa'], skladniki['jedMiary'], skladniki['cena'])
    print()


czytajdane()

