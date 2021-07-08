from datetime import date, time, datetime
print(date(year=2020, month=10, day=16))
print(time(hour=13, second=31, minute=50))
print(datetime(year=2020, month=10, day=16, hour=13, second=31, minute=50))

print(date.today())
now = datetime.now()
print(now)
current_time = time(now.hour, now.minute, now.second)
print(datetime.combine(date.today(), current_time))

print(date.fromisoformat("2021-07-08"))
d1 = "01-31-2021 13:47:21"
fmt = "%m-%d-%Y %H:%M:%S"

print(datetime.strptime(d1, fmt))

#import dateparser
#print(dateparser.parse("yesterday"))

# Working with timezones.
from dateutil import tz
from datetime import datetime, timedelta

now = datetime.now(tz=tz.tzlocal())
print(now)
print(now.tzname())

london_tz = tz.gettz("Europe/London")
print(london_tz)
gb_time = datetime.now(tz=london_tz)
print(gb_time)

now = datetime.now()
tomorrow = timedelta(days=+2, hours=-2)
print(now)
print(tomorrow)
print(now+tomorrow)
