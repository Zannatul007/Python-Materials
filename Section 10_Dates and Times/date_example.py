import datetime
import locale
locale.setlocale(locale.LC_ALL,'fr_FR.utf-8')
start = datetime.date(2022,4,2)
print(start)


pretty_start = start.strftime('%A %d %B,%Y')
print(pretty_start)

year = start.year
month = start.month
day = start.day
print(year,month,day)

today = datetime.date.today()
print(today)


print(today.strftime('%A'))
print(today.weekday())