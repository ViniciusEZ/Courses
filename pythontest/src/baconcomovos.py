"""
1 - receber um número inteiro

2 - O número é multiplo de 3 e 5
    Bacon com ovos
    
3 - Saber se o número não é multiplo de 3 e 5
    Passa fome
    
4 - Saber se o número é multiplo somente de 3
    Bacon
    
5 - Saber se o número é multiplo somente de 5
    Ovos
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser um inteiro.'
    
    if n % 15 == 0:
        return 'Bacon com ovos'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'
    
    return 'Passar fome'