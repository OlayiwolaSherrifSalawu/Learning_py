# learning recursion in python 

def bmi(weigth, higth):
    bmis= weigth/higth**2
    return bmis

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
# print(ft_and_inch_to_m(6))

def factorial(n):
    if n == 1 :
        return 1
    else :
     return   n* factorial(n-1)
 
print(factorial(5))