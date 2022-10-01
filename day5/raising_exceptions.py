def division(n1, n2):
    if n2 == 0:
        raise ValueError("n2 can't be 0")
    return n1 / n2
try:
    print(division(1,0))
except ValueError as error:
    print(error)