class IsWrongError(Exception):
    pass


def test():
    raise IsWrongError('WRONG!')


try:
    test()
except IsWrongError as e:
    print(f'Error: {e}')