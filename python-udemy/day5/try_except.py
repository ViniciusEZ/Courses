try:
    a = []
    print(a)
except (IndexError, KeyError) as erro:
    print(f'Erro de índice ou chave.')
except NameError as erro:
    print(f'Erro: {erro}')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Código executado com sucesso!')
finally:
    print('I always occur, so anyway!')