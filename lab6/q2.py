import datetime

now = datetime.datetime.now()
birth = datetime.datetime(1994, 5, 5, 0, 0, 0)

time = now - birth
print(time.days, "days,", "%d:%d:%d" %(now.hour, now.minute, now.second))

