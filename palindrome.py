def palindrome(stre:str):
    stre= stre.strip().lower()
    i=0
    j= len(stre)-1
    while i != len(stre)-1 and j !=0:
        if stre[i]!= stre[j]:
            return f"this is not a palindrome"
    return f"it is a palindrome"