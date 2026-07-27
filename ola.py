hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
print("this is a list ", hat_list)
mid =len(hat_list)//2
num= int(input("enter a number to be place at a middle"))
hat_list[mid]=num
# Step 2: write a line of code that removes the last element from the list.
print("current length",len(hat_list))
del hat_list[len(hat_list)-1]
# Step 3: write a line of code that prints the length of the existing list.
print("deleted list", len(hat_list))
print(hat_list)