import datetime
a = datetime.datetime.today()
print(a)
a = a + datetime.timedelta(days=1)
print(a)
a = a + datetime.timedelta(days=-2)
print(a)