"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento dos operadores com classes definidas pelo usuário.
"""


class Retangule:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + self.y
        return Retangule(new_x, new_y)

    def __repr__(self):
        return f"<class Retangulo({self.x}, {self.y})>"

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False


r1 = Retangule(11, 20)
r2 = Retangule(15, 20)
r3 = r1 + r2
print(r1 == r2)
