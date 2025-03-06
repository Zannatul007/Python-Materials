import datetime
tday = datetime.datetime.today()
tday_str = tday.strftime('%A %d %B %Y')
diff = datetime.timedelta(days=15,hours=48,minutes=60)

print(diff)
print(tday+diff)

d1  = datetime.timedelta(minutes=120)
d2 = datetime.timedelta(hours=2)
d3 = datetime.timedelta(seconds=7200)

print(d1,d2,d3,sep = ',')
print(repr(d1),repr(d2),repr(d3),sep=',')