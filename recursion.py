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
 
#  factorial with for loops 
def factorialF(n):
    if n < 1:
        return None
    elif n < 2 :
        return 1
    else:
        product =1
        for i in range(2,n+1):
            product*=i
        return product
# print(factorial(5),factorialF(6))

# # tuples
# des= (1,3,45,)
# print(des.count(1))
# faboniccii with recursion 
def fabonicci(n:int):
    if n == 1:
        return 1
    if n== 2:
        return 1
    return fabonicci(n-1)+fabonicci(n-2)

# fibonacci with loops 
def fibonacii_f(n:int) :
    if n == 1:
        return 1
    elif n== 2:
        return 1
    fabi=1
    fabp=1
    fbc=1
    for i in range(1,n-1):
        fabi=fabp+fbc
        
        fabp=fbc
        fbc=fabi

print(fabonicci(6))