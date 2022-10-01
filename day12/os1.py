import os

path_search = input('Type a path: ')
term_search = input('Type a term: ')
c = 0


def format_size(size):
    base = 1000
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'

    size = round(size, 2)
    return f'{size}{text}'


for root, directory, files in os.walk(path_search):
    for file in files:
        if term_search in file:
            try:
                c += 1
                full_path = os.path.join(root, file)
                file_name, ext_file = os.path.splitext(file)
                size_file = os.path.getsize(full_path)
                print()
                print(f'I found the file: {file}')
                print(f'Path: {full_path}')
                print(f'name: {file_name}')
                print(f'Extension: {ext_file}')
                print(f'Size: {size_file}')
                print(f'Format Size: {format_size(size_file)}')
            except PermissionError as e:
                print('Not Permission')
            except FileNotFoundError as e:
                print('File not Found')
            except Exception as e:
                print(f'Unknown error: {e}')
print()
print(f'{c} file(s) founded')
