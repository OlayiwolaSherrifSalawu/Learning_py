def cipher(word:str, num:int):
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

    



