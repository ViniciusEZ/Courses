# class Archive:
#     def __init__(self, file, mode):
#         print('Opening archive')
#         self.file = open(file, mode)
#
#     def __enter__(self):
#         print('Returning archive')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Closing archive')
#         self.file.close()
#         #Tratei a excessão
#
#
#
# with Archive('abc.txt', 'w+') as file:
#     file.write('Random Stuff')

from contextlib import contextmanager


@contextmanager
def opening(file, mode):
    try:
        print('Opening file')
        file = open(file, mode)
        yield file
    finally:
        print('Closing file')
        file.close()

with opening('abc.txt', 'a+') as file:
    file.write('Line1\n')
    file.write('Line2\n')
    file.write('Line3\n')
