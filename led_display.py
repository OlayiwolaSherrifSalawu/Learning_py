# hard wayyyyyy
digits = {"0": '1111110',  	# 0
	  "1": '0110000',	# 1
	 "2":  '1101101',	# 2
	  "3": '1111001',	# 3
	  "4": '0110011',	# 4
	  "5": '1011011',	# 5
	  "6": '1011111',	# 6
	  "7": '1110000',	# 7
	  "8": '1111111',	# 8
	 "9" : '1111011',	# 9
}
# bits= '0110011'
# 
def row_function(bits:str,index):
	rows={
          "0": (' 'if bits[0]=='0'and bits[6]=='0'and bits[3]=='0'else '#') + ('#' if bits[0]=='1' else ' ') + '#',
	"1": ('#' if bits[5]=='1' else ' ') + ' ' +('#' if bits[1]=='1' else ' '),
     "2":('#' if (bits[0]=='1' and (bits[1]=='1'or bits[5]=='1')) or (bits[5]=='1'and bits[1]=='1' and bits[0]=='0') else ' ') + ('#' if bits[6]=='1' else ' ') + '#',
     "3": ('#' if bits[4]=='1' else ' ') + ' ' +('#' if bits[2]=='1' else ' '),
     "4": ('##' if bits[3]=='1' else '  ')+'#',
     
	   }
	return rows[index]

def print_led_hard(nums:str):
     for i in range(5):
        for k in nums:
            print(row_function(digits[k],str(i)), end=" ")
        print()
        i+=1
          
     
# easy way
map= {
   "0": ["###", "# #", "# #", "# #", "###"],
   "1": ["  #","  #", "  #","  #","  #"],
   "2": ["###","  #", "###","#  ","###"],
   "3": ["###","  #", "###","  #","###"],
   "4": ["# #","# #", "###","  #","  #"],
   "5": ["###","#  ", "###","  #","###"],
   "6": ["###","#  ", "###","# #","###"],
   "7": ["###","  #", "  #","  #","  #"],
   "8": ["###","# #", "###","# #","###"],
   "9": ["###","# #", "###","  #","###"],
   }



def print_led_easy(num:str):
    for i in range(5):
        for k in num:
            val=map[k]
            print(val[i],end=" ")
        print()
        i+=1

# print_led_easy("689")
print_led_hard("577")