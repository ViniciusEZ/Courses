def singleton(the_class):
    instances = {}
    
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    
    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '20px'
        
@singleton
class Test:
    def __init__(self):
        print('Oi')
    
if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema verde'
    
    print(as1.tema)
    
    as2 = AppSettings()
    print(as1.tema)
    
    t1 = Test()
    t2 = Test()