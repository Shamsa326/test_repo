

#Creating the board with numbers and display it to the players:

board=[0,1,2,3,4,5,6,7,8]

player ="X"
moves =0 


while True:
    print(board[0],"|",board[1],"|",board[2])
    print(board[3],"|",board[4],"|",board[5])
    print(board[6],"|",board[7],"|",board[8])
    print()
      # try and except if you put a number or character not in the board 
    try:
        pos = int(input("Choose from 0-8:"))
     
    # check if position is taken
        if board[pos] in ["X","O"]:
          print("Position taken")
          continue

        board[pos]= player   
        moves=moves+1 
    except Exception:
       continue

    # switch player
    if player == "X":
     player = "O"
    else:
     player = "X"

    # stop after 9 moves
    if moves == 9:
        print("9 moves done")
        break

   