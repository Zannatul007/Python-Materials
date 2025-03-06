import datetime
import locale

# locale.setlocale(locale.LC_ALL,'fr_FR.utf-8')
today = datetime.datetime.today()
print(today)
today_str = today.strftime('%A %d %B %Y')
print(today_str)
print(today.strftime('%A'))
print(today.weekday())
print(today.isoweekday())