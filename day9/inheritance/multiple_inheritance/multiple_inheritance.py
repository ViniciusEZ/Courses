class A:
    def talk(self):
        print("Talking...I'm in A")


class B(A):
    def talk(self):
        print("Talking...I'm in B")


class C(A):
    def talk(self):
        print("Talking...I'm in C")


class D(B, C):
    ...
def talk(self):
    super().talk()
    print("Talking...I'm in C")
