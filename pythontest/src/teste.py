from calc import soma
#print(soma(-2, 5))
#print(soma(-5.5, 5))
#print(soma(-5.5, 10))

try:
    print(soma(20, 10))
except AssertionError as e:
    print(f'Conta inválida: {e}')

    
print('Olá mundo')

