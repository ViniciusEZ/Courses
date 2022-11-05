def soma(x, y): 
    """ Soma x e y
    
    >>> soma(10, 20)
    30
    
    >>> soma(-10, 30)
    20
    
    >>> soma('10', 30)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser um inteiro ou decimal.
    """
    assert isinstance(x, (int, float)), 'X precisa ser um inteiro ou decimal.'
    assert isinstance(y, (int, float)), 'Y precisa ser um inteiro ou decimal.'
    return x + y 

def subtrai(x, y):
    """ Subtraindo x e y
    >>> subtrai(10, 5)
    5
    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser um inteiro ou decimal.
    """
    assert isinstance(x, (int, float)), 'X precisa ser um inteiro ou decimal.'
    assert isinstance(y, (int, float)), 'Y precisa ser um inteiro ou decimal.'
    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    