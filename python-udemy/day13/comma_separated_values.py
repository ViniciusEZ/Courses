"""
Comma Separated Values - CSV (valores separados por vírgula)
é um formato de dados muito usado em tabelas (Excel, Google Sheets),
bases de dados, clientes de e-mail, etc...
"""
import csv

with open('clients.csv', 'r') as file:
    datas = [f for f in csv.DictReader(file)]
    # next(datas)
    # for data in datas:
    #     print(data['name'], data[' e-mail'])

with open('client2.csv', 'w+') as files:
    escreve = csv.writer(
        files,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chav = datas[0].keys()
    chav = list(chav)

    escreve.writerow(
        [
            chav[0],
            chav[1],
            chav[2],
            chav[3],
        ]
    )

    for data in datas:
        escreve.writerow(
            [
                data['name'],
                data[' lastname'],
                data[' e-mail'],
                data[' telephone']
            ]
        )

# for data in datas:
#     print(data)
