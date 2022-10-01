#!/usr/bin/env python3
import sys
import os


argus = sys.argv
qtd_argus = len(argus)

if qtd_argus <= 1:
    print('Missing arguments!')
    print('-a, Para listar todos os arquivos nesta pasta.')
    print('-d, Para listar todos os diretórios nesta pasta.')
    sys.exit()

only_arcs = False
only_dirs = False

if '-a' in argus:
    only_arcs = True

if '-d' in argus:
    only_dirs = True

for archive in os.listdir('.'):
    if only_arcs:
        if os.path.isfile(archive):
            print(archive)
    if only_dirs:
        if os.path.isdir(archive):
            print(archive)
