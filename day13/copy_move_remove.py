import os
import shutil

original_path = '/home/vinicius/Documents/teste'
new_path = '/home/vinicius/Documents/udemyPython2'

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f'Folder {new_path} already exists.')

for root, dirs, files in os.walk(new_path):
    for file in files:
        new_file_path = os.path.join(new_path, file)
        old_file_path = os.path.join(root, file)
        if '.py' in file:
            os.remove(new_file_path)
            # shutil.copy(old_file_path, new_file_path)
            # shutil.move(old_file_path, new_file_path)
            # print(f'File {file} copied sucessfully.')
