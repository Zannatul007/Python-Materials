import datetime

d = datetime.date(2025,3,6)
print(d)

dt = datetime.time(10,40,58,58000)
print(dt)

dtt = datetime.datetime(2025,3,6,10,40,58,58000)
print(dtt)

tday = datetime.date.today()
print(tday)
tday_time = datetime.datetime.today()
print(tday_time)

#timedelta 
tdelta = datetime.timedelta(days = 7)
print(tday_time+tdelta)

bday = datetime.date(2025,10,8)
print(bday - tday)

bday_timedelta = datetime.timedelta(days = 216)
print(tday+bday_timedelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
