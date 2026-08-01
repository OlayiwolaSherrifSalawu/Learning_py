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

board[1][1]= "X"
print(board, end="\n")
def reduce_list(lst:list, num):
     if num in lst:
          n = lst.index(num)
          del lst[n]
     return lst
def  cal_row_col(num:int):
    row=num//3
    col = (num%3)-1
    if col <0:
         row+=col
    return row, col
def fixs_O(lst:list, num:int):
     row,col=cal_row_col(num)
     lst[row][col]="O"
     return lst
def fix_O(num):
     cal_row_col(num)


print(cal_row_col(9))