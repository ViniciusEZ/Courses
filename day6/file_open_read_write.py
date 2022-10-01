import json
d1 = {
    "Person 1": {
        "Name" : "Luiz",
        "Age" : 25
    },
    "Person 2": {
        "Name": "Maria",
        "Age": 46
    },

}

d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
print(d1_json)
# os.remove('abc.txt')
# with open('abc.txt', 'a+') as file:
#     file.write('Alguma coisa\n')
#     file.seek(0,0)
#     print(file.read())

# file.write('Random Stuff\n')
# file.write('Random Stuff\n')
# file.write('Random Stuff\n')
# file.seek(0,0)
# print(file.read())
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# for line in file.readlines():
#     print(line, end='')



