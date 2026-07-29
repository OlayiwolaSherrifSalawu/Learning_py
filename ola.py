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
def add_half_naira(price):
    return price + 0.50

# Equivalent Lambda Function
# Syntax: lambda input_variable: expression_to_return
lambda_tax = lambda price: price + 0.50
print(lambda_tax)