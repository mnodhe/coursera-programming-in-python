import calendar
import sys
locations = sys.path
print(locations)

for item in locations:
    print(item)


leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isItLeap=calendar.isleap(2040)
print(isItLeap)