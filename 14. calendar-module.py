import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    # month, day, year = 8, 5, 2015
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())
