# tic tac toe

board =[[i for i in range(1,4)]for r in range(3)]
i = 1
maxs=0
while i < len(board):
     maxs =  board[i-1][len(board[i])-1]
     for k in range(len(board[i])):
          board[i][k]= maxs+1
          maxs=  board[i][k]
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


print(cal_row_col(9))