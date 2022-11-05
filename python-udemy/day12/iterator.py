class MyList:
    def __init__(self):
        self._items = []
        self._index = 0

    def push(self, value):
        self._items.append(value)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        if index >= len(self._items):
            self._items.append(value)
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self._items[self._index]
            self._index += 1
            return item
        except IndexError as e:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__} {self._items}'


li = MyList()
li.push(1)
li.push(2)
li.push('Vinicius')
li = list(li)
# li[3] = 'Nada'
# del li[3]
# print(li)
for value in li:
    print(value)
for value in li:
    print(value)



