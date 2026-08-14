def cipher(word:str, num:int):
    text=""
    for char in word:
        if not char.isalpha():
            text += char
            continue
        code = ord(char) +num
        if  char.upper():
            if code > ord('Z'):
                code = code- ord('Z')+ord('A')
        elif char.lower():
            if code > ord('z'):
                code = code- ord('z')+ord('a')
        text += chr(code)
    return text
    

def collectValue():
    word = input("enter a word you would like to cipher: ")
    num=0
    try: 
        num= int(input("Enter a cipher key between 1-25 ensure it is a number: "))

    except ValueError:
        print("please ensure you enter a number: ")
    if num<1 or num >25: 
        print("please follow the instruction and dont act like an animal")
        return None,None
    return word, num 


words,nums= collectValue()
text=cipher(words,nums)
print(text)