def digit_of_life(str2:str):
    if len(str2)== 1:
        return str2
    total=0
    for i in str2:
        total+= int(i)
    return digit_of_life(str(total))


def validate(str2:str):
    for i in str2 :
        if i.isalpha():
            return False

def collect_args():
    values = input("enter you date of birth in this format YYYYDDMM: ")
    return values

words=collect_args()
valid= validate(words)
if not valid:
    print("please ensure the value you pass are all number no letters please")

if valid:
    print(digit_of_life(words))