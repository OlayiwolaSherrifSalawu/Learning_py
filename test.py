
# writing my split function 
def mysplit(word:str):
    lst= []
    
    if len(word)== 0:
        return lst
    new_word= ""
    for i in word:
        if new_word =="" and i != " ":
            new_word+=i
        elif new_word !="" and i != " ":
            new_word+= i
        elif new_word !="" and (i == " " or i == "\n"):
            lst.append(new_word)
            new_word=""
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
    