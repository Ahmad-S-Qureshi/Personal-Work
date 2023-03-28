from datetime import date, timedelta, time

def read_date():
    str_in = input()
    tokens = str_in.split('-')
    currdate = date(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    return currdate

date1 = read_date()
date2 = read_date()
date3 = read_date()
date4 = read_date()
daysList = [date1, date2, date3, date4]

for day in sorted(daysList):
    print(f'{day.month:02.0f}/{day.day:02.0f}/{day.year:02.0f}')

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number
timedelta = sorted(daysList)[(len(daysList)) - 1] - sorted(daysList)[len(daysList) - 2]
print(timedelta.days)

# 6. Output the date that is 3 weeks from the most recent date in the list
delta = timedelta(days = 27)
print(sorted(daysList)[(len(daysList)) - 1] + delta)

# 7. Output the full name of the day of the week of the earliest day
