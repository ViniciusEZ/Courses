from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays



setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
current_month = int(dt.strftime('%m'))
formatar1 = dt.strftime('%A, %d de %B de %Y')
formatar2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatar1)
print(current_month, mdays[current_month])



