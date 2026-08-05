my_list = [1,2]

for v in range(2):
     my_list.insert(-1,my_list[v])

del my_list[:]    
print(my_list)