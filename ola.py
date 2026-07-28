board = [["EMPTY" for i in range(8)] for j in range(8)]

board[0][0]="ROOK"
board[0][7]="ROOK"
board[7][0]="ROOK"
board[7][7]="ROOK"
for i in range(len(board[1])):
    board[1][i]="pawn"
    board[6][i]="pawn"
print(board)