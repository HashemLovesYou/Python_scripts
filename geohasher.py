import datetime as dt
from antigravity import geohash

today = dt.date.today()
month1 = str(today.month)
day1 = str(today.day)
month = month1.zfill(2)
day = day1.zfill(2)
DJIA = input("Enter today's DJIA open: ")

geohash(40, -74, f'{today.year}-{month}-{day}-{DJIA}'.encode('utf-8'))
