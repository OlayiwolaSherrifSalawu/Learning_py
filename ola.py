# leap year checker 
year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    if year%400==0:
          print("It is a leap year")
    elif year%100==0:
          print("it is a common year")
    elif year%4==0:
          print("It is a leap year")
    else:
          print("it is a common year")