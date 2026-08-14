def split_word(str2:str):
    lst =[]
    for i in range(len(str2)):
        lst.append(str2[i])
    return lst
def anagram(str1:str, str2s:str):
   
   st1= sorted(split_word(str1))
   st2= sorted(split_word(str2s))
   if "".join(st1)=="".join(st2):
       return f"this words are anagram"
   else:
       return f"this words arent anagrams"
    
   
def clean_string(str1:str, str2:str):

    word1, word2= str1.replace(" ","").lower(), str2.replace(" ","").lower()
    return word1,word2
def collect_arg():
    first = input("enter a word: ")
    second = input("enter another word: ")
    return first, second


word1, word2= collect_arg()
word1s,word2s= clean_string(word1,word2)
print(anagram(word1,word2))

