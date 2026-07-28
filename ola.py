board = [["EMPTY" for i in range(8)] for j in range(8)]

board[0][0]="ROOK"
board[0][7]="ROOK"
board[7][0]="ROOK"
board[7][7]="ROOK"
for i in range(len(board[1])):
    board[1][i]="pawn"
    board[6][i]="pawn"
print(board)

# an hotel with three building and each has about 15 floors and 20 rooms on each floor 
#  this is a three d array and i can do it like this 

rooms= [[[False for r in range(20)] for f in range(15)]for b in range(3)]
print(rooms)