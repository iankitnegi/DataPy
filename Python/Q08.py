#Program to display calendar

import calendar
y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
c = calendar.month(y, m)
print(c)