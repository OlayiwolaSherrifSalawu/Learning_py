# tic tac toe
import random
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
     coordinates= {
          1:{
          "top":(2,3,1),
          "side":(4,7,1),
          "diagonal": (1,5,9)
     },
          3:{
          "top":(2,1,3),
          "side":(5,7,3),
          "diagonal": (6,9,3)
     },
          7:{
          "top":(7,8,9),
          "side":(1,4,7),
          "diagonal": (7,5,3)
          },
          9:{
          "top":(7,8,9),
          "side":(9,6,3),
          "diagonal": (9,5,1)
          },
          # this are the inplace diagonals
          2:{
          "top":(1,2,3),
          "side":(2,5,8),
          },
          4:{
          "top":(4,5,6),
          "side":(1,4,7),
          },
          6:{
          "top":(4,5,6),
          "side":(3,6,9),
          },
          8:{
          "top":(2,5,8),
          "side":(7,8,9),
          },
          
     }
     
     diagonal= coordinates[num]
     for vals in diagonal.values():
          r1,c1=cal_row_col(vals[0])
          r2,c2= cal_row_col(vals[1])
          r3,c3= cal_row_col(vals[2])
          if (board[r1][c1] == board[r2][c2]==board[r3][c3]):
               return "win"
    


def display_board(board:list):
     for i in board:
          print(i)

status= ""
boards[1][1]="X"
playing_list= [1,2,3,4,6,7,8,9]
while status!="WIN" or status != "LOOSE":
     
     display_board(boards)
     print()
     try:
          move= int(input("Enter Your move: "))
     except ValueError:
          print("Only Integers allowed.")
    
     try:
          if move not in playing_list:
               print("cant play this number")
               continue
     except NameError:
          print("enter a value pls")
     row,col=cal_row_col(move)
     
     boards[row][col]="O"
     reduce_list(playing_list,move)
     # print(boards)
     status=diagonal_win(boards,move)
     # print(status)
     if status=="win":
          display_board(boards)

          print("You Won")

          status="WIN"
          break
     num= random.choice(playing_list)
     row,col=cal_row_col(num)
     boards[row][col]="X"
     # display_board(boards)
     reduce_list(playing_list,num)
     status=diagonal_win(boards,num)
     # print(status)
     if status=="win":
          display_board(boards)
          print("You Loose")
          status="LOOSE"
          break
     if len(playing_list)<1:
          print("it is a draw ")
          break




