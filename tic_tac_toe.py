# tic tac toe

boards =[[i for i in range(1,4)]for r in range(3)]
i = 1
maxs=0
while i < len(boards):
     maxs =  boards[i-1][len(boards[i])-1]
     for k in range(len(boards[i])):
          boards[i][k]= maxs+1
          maxs=  boards[i][k]
     i+=1

def reduce_list(lst:list, num):
     if num in lst:
          n = lst.index(num)
          del lst[n]
          return lst
     else:
          return None
def  cal_row_col(num:int):
    row=num//3
    col = (num%3)-1
    if col <0:
         row+=col
    return row, col
def fixs_vals(board:list, num:int,val):
     row,col=cal_row_col(num)
     board[row][col]=val
     return board

# the win helper functions
"""
the idea is by default i have a list of [1,2,3,4,6,7,8,9]
"""

# i would have to write the win two functions to check 
def diagonal_win(board:list, num:int):
     if num==1 or num==3:
          diagonal1= {
               "top":(2,3,1),
               "side":(4,7,1),
               "diagonal": (1,5,9)
          }
          diagonal3= {
               "top":(2,1,3),
               "side":(5,7,3),
               "diagonal": (6,9,3)
          }
          diagonal= {}
          if num==1:
               diagonal= diagonal1
          else:
               diagonal= diagonal3
          for vals in diagonal.values():
               r1,c1=cal_row_col(vals[0])
               print(vals[0],r1,c1)
               r2,c2= cal_row_col(vals[1])
               r3,c3= cal_row_col(vals[2])
               if (board[r1][c1] == board[r2][c2]==board[r3][c3]):
                    return "you won"

boards[0][2],boards[1][2]=boards[2][2],boards[2][2]
print(boards)
print(diagonal_win(boards,3))
