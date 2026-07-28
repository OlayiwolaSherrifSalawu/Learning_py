my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list= []
print("The list with unique elements only:")
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
