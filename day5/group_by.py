from itertools import count, groupby, tee

students = [
    {'name': 'Luiz', 'grade': 'A'},
    {'name': 'Maria', 'grade': 'B'},
    {'name': 'Vinicius', 'grade': 'A'},
    {'name': 'Beatriz', 'grade': 'C'},
    {'name': 'Carlos', 'grade': 'A'},
    {'name': 'Sofia', 'grade': 'C'},
    {'name': 'Renato', 'grade': 'A'},
    {'name': 'Beato', 'grade': 'B'},
    {'name': 'Jay', 'grade': 'A'},
    {'name': 'Magno', 'grade': 'B'},
    {'name': 'Jairo', 'grade': 'C'}
]
order = lambda n: n['grade']
students.sort(key=order)
grouped_students = groupby(students, order)

for grouping, grouped_values in grouped_students:
    va1, va2 = tee(grouped_values)
    print(f'grouping: {grouping}')

    for student in va1:
        print(student)

    qtde = len(list(va2))
    print(f'\t{qtde} alunos tiraram a nota {grouping}')
    print()

