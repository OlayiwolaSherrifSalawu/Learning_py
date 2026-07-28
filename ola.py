# my first function 

def message(name:str):
    print("hello!", name, "i Love you" )

name = input("Please enter your name: ")
message(name)

# favourite food 

def favFood(firstFood:str, secondFood:str, third:str):
    myFood = []
    myFood.append(firstFood,secondFood,third)
    for i in myFood:
        if len(i)%2>2:
            print(i, "is a terible food")
        else:
            print("i love", i, "too")