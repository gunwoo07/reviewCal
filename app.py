from datetime import datetime, timedelta
from typing import final


repeats = [1, 2, 7, 14, 31, 62]
class color:
    Purple = '\033[95m'
    Cyan = '\033[96m'
    Darkcyan = '\033[36m'
    Blue = '\033[94m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    Bold = '\033[1m'
    Underline = '\033[4m'
    End = '\033[0m'
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


print(f'{color.Bold}복습 날짜 계산기📖 v1.0{color.End}')
year = input(f'{color.Bold}년: {color.End}')
month = input(f'{color.Bold}월: {color.End}')
day = input(f'{color.Bold}일: {color.End}')

finalDays = []
now = datetime.strptime(f'{year}{str(month).zfill(2)}{str(day).zfill(2)}', '%Y%m%d')

for re in repeats:
    a = (now + timedelta(days=-re))
    finalDays.append(a.strftime('%Y년 %m월 %d일') + f'({weekdays[a.weekday()]})')

print('')
print(f'{color.Bold}오늘 복습해야 하는 날들📆{color.End}')
for i, reDay in enumerate(finalDays):
    print(f'{color.Bold}[D+{str(repeats[i]).zfill(2)}]{color.End} {reDay}')
