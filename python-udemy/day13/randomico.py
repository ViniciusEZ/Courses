import random
import string

integer = random.randint(10, 100)
flutua = random.uniform(10, 100)
flutua2 = random.random()
integer2 = random.randrange(20, 50, 3)
# print(integer2)

name_sorteia = ['Vinicius', 'Maria', 'Jean', 'Rosa', 'Danilo', 'Micael']
# lista_sorteada = random.choices(name_sorteia, k=2)
# lista_sorteada1 = random.sample(name_sorteia, k=2)
# lista_sorteada2 = random.choice(name_sorteia, k=2)
random.shuffle(name_sorteia)
# Gera senha aleatória
letters = string.ascii_letters
digitz = string.digits
chars = "!@#$%¨&*()"
geral = letters + digitz + chars
password = ''.join(random.choices(geral, k=32))
print(password)


