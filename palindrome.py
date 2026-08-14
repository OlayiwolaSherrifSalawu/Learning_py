def palindrome(stre:str):
    stre= stre.strip().lower()
    i=0
    j= len(stre)-1
    
    while i != len(stre)-1 and j !=0:
        if stre[i]!= stre[j]:
            return f"this is not a palindrome"
        i+=1
        j-=1
    return f"it is a palindrome"


print(palindrome("Ten animals I slam in a net"))