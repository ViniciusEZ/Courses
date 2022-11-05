"""
Join - Função usada para juntar a thread criada com a thread principal (arquivo main).
"""
from time import sleep
from threading import Thread, Lock


class Tickets:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, amount):
        self.lock.acquire()

        if self.stock < amount:
            print("We don't have sufficient tickets.")
            self.lock.release()
            return

        sleep(1)

        self.stock -= amount
        print(f'You buy {amount} ticket(s). We still have {self.stock}'
              f' in stock.')

        self.lock.release()


if __name__ == '__main__':
    tic1 = Tickets(10)

    thread_list = []
    for i in range(1, 20):
        t = Thread(target=tic1.buy, args=(i,))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    executing = True
    while executing:
        executing = False

        for t in thread_list:
            if t.is_alive():
                executing = True
                break

    print(tic1.stock)

# def take_time(text, timer):
#     sleep(timer)
#     print(text)
#
#
# t = Thread(target=take_time, args=('Está executando', 10))
# t.start()
# t.join()
# print('Hello World!')


# while t.is_alive():
#     print('Waiting for Thread')
#     sleep(1)


# def take_time(text, timer):
#     sleep(timer)
#     print(text)
#
#
# t = Thread(target=take_time, args=('Está executando', 5))
# t.start()
# t2 = Thread(target=take_time, args=('Está executando2', 6))
# t2.start()
# t3 = Thread(target=take_time, args=('Está executando3', 7))
# t3.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)

# class MyThread(Thread):
#     def __init__(self, text, timer):
#         self.text = text
#         self.timer = timer
#         super().__init__()
#
#     def run(self):
#         sleep(self.timer)
#         print(self.text)
#
#
# textinho1 = MyThread('Minha Thread1', 15)
# textinho1.start()
#
# textinho2 = MyThread('Minha Thread2', 5)
# textinho2.start()
#
# textinho3 = MyThread('Minha Thread3', 10)
# textinho3.start()
#
#
#
# for i in range(30):
#     print(i)
#     sleep(1)
