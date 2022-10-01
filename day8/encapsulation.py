'''
public, protected, private
_ protected
__ private
'''


class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data


    def insert_client(self, id, name):
        if 'client' not in self.__data:
            self.__data['client'] = {id: name}
        else:
            self.__data['client'].update({id: name})

    def show_clients(self):
        for id, name in self.__data['client'].items():
            print(id, name)

    def delete_client(self, id):
        del self.__data['client'][id]


db = DataBase()
db.insert_client(1, 'Vinicius')
db.insert_client(2, 'Flávio')
db.insert_client(3, 'Amarildo')
db.insert_client(4, 'Jason')
db.__data = 'Random Stuff'
print(db.data)
print(db._DataBase__data)
db.show_clients()

