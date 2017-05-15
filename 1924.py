import datetime

weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', ]

month, day = input().split(' ')
month, day = int(month), int(day)

wanted_day = datetime.datetime(year=2007, month=month, day=day)
print(weekday[wanted_day.weekday()])
