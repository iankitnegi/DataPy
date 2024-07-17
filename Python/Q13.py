#Program to check leap year

y = int(input("Enter the year: "))

if y%400==0 and y%100==0:
    print("{0} is a leap year".format(y))
elif y%4==0 and y%100!=0:
    print("{0} is a leap year".format(y))
else:
    print("{} is not a leap year".format(y))