"""Just some time pass"""
from datetime import datetime
now = datetime.now()
nyear = now.year
nmonth = now.month
nday = now.day
dobyear = 1999
dobmonth = 04
dobday = 30
age = nyear - dobyear
print ("The Legend Rishil was born on %s-%s-%s and today on %s-%s-%s he is %s years old. ") \
      % (dobday,dobmonth,dobyear,nday,nmonth,nyear,age)
print now
