import math
# class KitchenCalculator:
#     def calculate_inventory(self):
#         customers = 3
#         cereal_per_customer = 2.5
#         milk_per_customer = 1.25
        
#         starting_cereal = 10.0
#         starting_milk = 15.0
        
#         # 1. Use multiplication to calculate the totals needed
#         total_cereal = customers* cereal_per_customer
#         total_milk = customers*milk_per_customer
        
#         # 2. Use subtraction to calculate the remaining inventory
#         remaining_cereal = starting_cereal-total_cereal
#         remaining_milk = starting_milk-total_milk
        
#         return math.ceil(remaining_cereal), math.ceil(remaining_milk)


# class LayiClass:
#     def __init__(self, names):
#         self.name= names
#     def sing(self):
#         print(f"{self.name} is singing and needs help")

# Standard Function Definition
# def add_half_naira(price):
#     return price + 0.50

# Equivalent Lambda Function
# Syntax: lambda input_variable: expression_to_return
lambda_tax = lambda price: price + 0.50
lambda_name= lambda name:  print(f"hello {name}")
# lambda_name("olayiwola")
# print(lambda_tax(45))

# tuples 
var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
# print(t1, t2, t3)
# dictionaries in python 

# pydic= {
#     "ola":"Jesus",
#     "salawu":"God",
#     "bise":"John"
# }
# print(pydic["ola"])
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
 
# for keyss, vals in dictionary.items():
#     print(keyss, "->", vals)


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = {}
for i in tup:
  if i in duplicates.keys():
    duplicates[i]+=1
  else:
    duplicates[i]=1
higest=0
key=0
for keys,val in duplicates.items():
  if val>higest:
    higest=val
    key=keys
  

print(duplicates,"\n",f"key with highest count {key} -> {higest}") # outputs: 4