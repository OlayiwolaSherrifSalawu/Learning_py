def split_word(str2:str):
    lst =[]
    for i in str2:
        lst.append(i)
    return lst
def anagram(str1:str, str2:str):
   
   st1= sorted(split_word(str1))
   st2= sorted(split_word(str2))
   if "".join(st1)=="".join(st2):
       return f"this words are anagram"
   else:
       return f"this words arent anagrams"
    
   
def clean_string(str1:str, str2:str):
    return str1.replace(" ","").lower,str2.replace(" ","").lower

def collect_arg():
    first = input("enter a word: ")
    second = input("enter another word: ")
    return first, second


# word1, word2= collect_arg()
# word1,word2= clean_string(word1,word2)
# print(anagram(word1,word2))

print(anagram("silent","listen"))