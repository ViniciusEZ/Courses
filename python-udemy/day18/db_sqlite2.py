import sqlite3


class AgendaDB:
    def __init__(self, archive):
        self.con = sqlite3.connect(archive)
        self.cursor = self.con.cursor()

    def insert(self, name, telephone):
        consult = 'INSERT OR IGNORE INTO agenda (name, telephone) VALUES(?, ?)'
        self.cursor.execute(consult, (name, telephone))
        self.con.commit()

    def update(self, name, telephone, id):
        consult = 'UPDATE OR IGNORE agenda SET name=?, telephone=? WHERE id=?'
        self.cursor.execute(consult, (name, telephone, id))
        self.con.commit()

    def delete(self, id):
        consult = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.con.commit()

    def search(self, value):
        consult = 'SELECT * FROM agenda WHERE name LIKE ?'
        self.cursor.execute(consult, (f'%{value}%',))
        for linha in self.cursor.fetchall():
            print(linha)

    def show(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def close(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    agenda = AgendaDB('/home/vinicius/Documents/udemyPython/day18/agenda.db')
    agenda.search('Maria')
