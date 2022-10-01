carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20.50))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 100))
carrinho.append(('Produto 5', 100))

total = sum([float(x[1]) for x in carrinho])
print(total)
