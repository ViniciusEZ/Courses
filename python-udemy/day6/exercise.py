reserve = []
list_assingment = []


def add(p1):
    reserve.append(p1)
    list_assingment.append(p1)


def show():
    print()
    print('List of assingments: ')
    print(f'{list_assingment}')
    print()


def undo():
    if not list_assingment:
        print('Nada para ser desfeito!')
        return []
    list_assingment.append(reserve[len(list_assingment)])


def redo():
    if not list_assingment:
        print('Nada para ser retirado!')
        return []
    list_assingment.pop()


while True:
    user = input("Select an option - add, show, undo, redo: ")

    if user == 'add':
        user2 = input("Digite o item a ser adicionado: ")
        add(user2)
    if user == 'show':
        show()
    if user == 'undo':
        undo()
    if user == 'redo':
        redo()
