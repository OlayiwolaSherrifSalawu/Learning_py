def find_word(s1:str,s2:str):
    flag= False
    for i in s1:
        flag=True
        for j in s2:
            if s1[i]==s2[j]:
                s2=s2[j:]
                flag= False
                continue
    if flag:
        return f"NO"
    else:
        return f"YES"
    