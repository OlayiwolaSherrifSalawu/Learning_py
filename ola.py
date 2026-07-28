# my first function 

def message(name:str):
    print("hello!", name, "i Love you" )

name = input("Please enter your name: ")
message(name)

# favourite food 

def favFood(myFood):
    for i in myFood:
        if len(i)%2>2:
            print(i, "is a terible food")
        else:
            print("i love", i, "too")
            

firstFood=  input("input three food you love: ")
strd= ""
myList= []
for i in firstFood:
    if i==" " and strd == "":
        continue
    if i !=" ":
        strd+=i
    elif i == " "  and strd != "":
        myList.append(strd)
        strd=""
        
        
favFood(myList)