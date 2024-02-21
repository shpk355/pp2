import datetime

d= datetime.timedelta(days=5)
x = datetime.datetime.today() + d
print(x)
dif = datetime.timedelta(days=-1)
print((datetime.datetime.today()+dif))
print(datetime.datetime.today())
print((datetime.datetime.today()-dif))
y = x.replace(microsecond=0)
print(y)
print((x - datetime.datetime.today()).total_seconds())