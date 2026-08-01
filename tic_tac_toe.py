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


print(board)