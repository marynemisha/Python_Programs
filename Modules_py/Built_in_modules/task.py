import datetime
x=datetime.datetime.now()
print(x)

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%m-%d-%Y"))
print(x.strftime("%B %m,%Y"))
print(x.strftime("%Y %B %d"))
print(x.strftime("%Y %B %d,%H.%M%p"))
print(x.strftime("%A,%d-%B-%Y"))
print(x.strftime("%d-%B-%Y|%I:%M%p"))
print(x.strftime("%Y/%m/%d %H:%M"))
print("Today is",x.strftime("%A"),"the",x.strftime("%d"),"nd of" ,x.strftime("%B,%Y"))