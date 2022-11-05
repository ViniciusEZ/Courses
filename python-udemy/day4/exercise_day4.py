string = '0123456789012345678901234567890123456789'
lista = '.'.join([string[i:i+10] for i in range(0, len(string), 10)])
print(lista)
