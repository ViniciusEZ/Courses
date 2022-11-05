class A:
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_alreadyexist'):
    #         cls._alreadyexist = object.__new__(cls)
    #
    #     return cls._alreadyexist

    def __init__(self):
        pass

    # def __call__(self, *args, **kwargs):
    #     res = 1
    #     for i in args:
    #         res *= i
    #     return res

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    # def __del__(self):
    #     print('OBJETO DELETADO')

    def __str__(self):
        return "<class A>"

    def __len__(self):
        return 10





a = A()
a.name = 'Vinicius'
print(a.name)
print(a)
print(len(a))




