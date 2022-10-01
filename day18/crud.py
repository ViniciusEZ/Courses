import pymysql
from contextlib import contextmanager


@contextmanager
def conect():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='998688124cfAL@',
        db='Clients',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ("Sérgio", "Camargo", 100, 202.6))
#         connects.commit()

#
# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('Murilo', 'Fernandes', 23, 98.7),
#             ('Urias', 'Aragão', 34, 101),
#             ('Samara', 'Barroso', 13, 40),
#         ]
#
#         cursor.executemany(sql, dados)
#         connects.commit()


# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         connects.commit()

# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s)'
#         cursor.execute(sql, (5, 7))
#         connects.commit()

# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s and %s'
#         cursor.execute(sql, (8, 10))
#         connects.commit()

# with conect() as connects:
#     with connects.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('MATHIAS', 4))
#         connects.commit()



with conect() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id LIMIT 100')
        res = cursor.fetchall()

        for linha in res:
            print(linha)
