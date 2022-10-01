from time import time, sleep
# def master(func):
#     def slave(*args, **kwargs):
#         print("Now, I'm decorate")
#         func(*args, **kwargs)
#     return slave
#
# @master
# def speak_hello():
#     print('oi')
#
# @ master
# def other_function(msg):
#     print(msg)

# speak_hello = master(speak_hello)
# other_function("Hello, I'm Vinicius!")
# speak_hello()

def speed(func):
    def inside(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        time1 = (end_time - start_time) * 1000
        print(f'\nThe function {func.__name__} takes {time1:.2f} ms to execute. ')
        return res
    return inside

@speed
def take_time():
    for i in range(10):
        print(i, end='')


take_time()

