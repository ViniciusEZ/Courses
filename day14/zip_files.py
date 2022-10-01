from zipfile import ZipFile
import os

paths = '/home/vinicius/compactados'

with ZipFile('archive.zip', 'w') as zip:
    for archives in os.listdir(paths):
        full_path = os.path.join(paths, archives)
        zip.write(full_path, archives)

with ZipFile('archive.zip', 'r') as zipi:
    for archuve in zipi.namelist():
        print(archuve)

with ZipFile('archive.zip', 'r') as zip:
    zip.extractall('Descompactado')

