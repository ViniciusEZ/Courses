from datetime import datetime, timedelta

data1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('25/04/1987 23:35:00', '%d/%m/%Y %H:%M:%S')
print(data1.time())
print(data2 > data1)








# dif = data2 - data1
# print(dif.total_seconds())
# print(dif.days)
# data = data + timedelta(seconds=60*60)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))
# strptime('08/08/2022', '%d/%m/%Y')
# print(data.timestamp())
# print(data.strftime('%d/%m/%Y %H:%M:%S'))