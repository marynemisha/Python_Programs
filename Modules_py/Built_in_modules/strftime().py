import datetime
x=datetime.datetime.now()
print("Current date and time:",x)
print("Abbreviated weekend :",x.strftime("%a"))
print("Full weekend        :",x.strftime("%A"))
print("Abbreviated month   :",x.strftime("%b"))
print("Full month          :",x.strftime("%B"))
print("Local's AM or PM    :",x.strftime("%p"))
print("Year with century   :",x.strftime("%Y"))
print("Year with century as dec   :",x.strftime("%y"))
print("Year without century as dec  :",x.strftime("%y"))
print("Hour (24-hour clock) :",x.strftime("%H"))


#2026-07-22 09:52:23
print(x.strftime(("%Y-%m-%d %H:%M:%S")))

#Today is wednesday,July 22,2026
print("Today is",x.strftime("%A,%B %d,%Y"))

