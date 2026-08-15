digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]
bits= '0110011'
# 
row0= (' 'if bits[0]=='0'and bits[6]=='0'and bits[3]=='0'else '#') + ('#' if bits[0]=='1' else ' ') + '#'
row4 =  ('##' if bits[3]=='1' else '  ')+'#'
row1= ('#' if bits[5]=='1' else ' ') + ' ' +('#' if bits[1]=='1' else ' ')
row2= ('#' if (bits[0]=='1' and (bits[1]=='1'or bits[5]=='1')) or (bits[5]=='1'and bits[1]=='1' and bits[0]=='0') else ' ') + ('#' if bits[6]=='1' else ' ') + '#'
row3= ('#' if bits[4]=='1' else ' ') + ' ' +('#' if bits[2]=='1' else ' ')

# easy way
map= {
   "0": ["###", "# #", "# #", "# #", "###"]
   }