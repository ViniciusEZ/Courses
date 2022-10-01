def convert_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
           ...


number = convert_number(input('Type a number: '))
if number is not None:
    print(number * 5)
else:
    print('Unsuported operand!')