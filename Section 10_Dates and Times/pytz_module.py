import pytz
import datetime
dt_utcnow = datetime.datetime.now(tz = pytz.UTC)
print(dt_utcnow)

# dt_today = datetime.datetime.today()
# print(dt_today)

dt_mtn = dt_utcnow.astimezone((pytz.timezone('US/Eastern')))
print(dt_mtn)

# for tz in pytz.all_timezones:
    
#     if ("Dhaka" in tz):

#          print(tz)
# c = 0
# for tz in pytz.all_timezones:
#     c+=1
# print(c)
dt_mtn_bd = dt_utcnow.astimezone((pytz.timezone('Asia/Dhaka')))
print(dt_mtn_bd)



#naive datetime to timezone date
tday = datetime.datetime.now()
tday_tz = tday.astimezone(pytz.timezone('Asia/Dhaka'))
print(tday_tz)