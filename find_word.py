def find_word(s1:str,s2:str):
    flag= False
    for i in range(len(s1)-1):
        flag=True

        for j in range(len(s2)-1):
            print(i,j)
            if s1[i]==s2[j]:
                s2=s2[j:]
                flag= False
                break
            j+=1
        i+=1
    if flag:
        return f"NO"
    else:
        return f"YES"


print(find_word("donut","Nabucodonosor"))