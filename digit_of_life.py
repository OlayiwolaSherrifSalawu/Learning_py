def digit_of_life(str2:str):
    if len(str2)== 1:
        return str2
    total=0
    for i in str2:
        total+= int(i)
    return digit_of_life(str(total))


def validate(str2:str):
    for i in str2 :
        if i.isalnum():
            return False