# Store the current largest number here.
largest_number = -999999999
 
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
 
# If the number is not equal to -1, continue.

while number!= -1:
    if number > largest_number:
        largest_number= number
        print("large number",largest_number)
    number = int(input())

print("the lagest number =", largest_number)