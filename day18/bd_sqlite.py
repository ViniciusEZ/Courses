import sqlite3
con = sqlite3.connect('DataBase.db')
curso = con.cursor()
# curso.execute('CREATE TABLE IF NOT EXISTS Clients ('
#               'ID integer primary key autoincrement not null,'
#               'Name TEXT,'
#               'Weight REAL'
#               ')')


# curso.execute('INSERT INTO Clients (Name, Weight) VALUES'
#               '("Vinicius", 200)')
# curso.execute('INSERT INTO Clients (Name, Weight) VALUES'
#               '(?, ?)', ('Maria', 60))
#
# curso.execute('INSERT INTO Clients (Name, Weight) VALUES'
#               '(:Name, :Weight)', {'Name': 'Viktor', 'Weight': 90})
#
# curso.execute('INSERT INTO Clients VALUES'
#               '(:ID, :Name, :Weight)', {'ID': None, 'Name': 'Fernanda', 'Weight': 200})
# con.commit()


# curso.execute('UPDATE Clients SET Name=:Name WHERE ID=:ID',
#               {'Name': 'João', 'ID': 7}
#               )

# curso.execute('DELETE FROM Clients WHERE ID=:ID',
#               {'ID': 7}
#               )
# con.commit()

curso.execute('SELECT Name, Weight FROM Clients WHERE Weight>:Weight', {'Weight': 60})
for linha in curso.fetchall():
    name, weight = linha
    print(f'Name: {name}, Weight: {weight}')

curso.close()
con.close()
