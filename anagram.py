def anagram(str1:str, str2:str):
   st1= sorted(str1)
   st2= sorted(str2)
   if "".join(st1)=="".join(st2):
       return f"this words are anagram"
   else:
       return f"this words arent anagrams"
   