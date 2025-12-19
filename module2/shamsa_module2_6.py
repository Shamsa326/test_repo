

#Game 2048

#
import random

# create board
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# 2. add a random tile
def add_tile():
    pos = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                pos.append((i, j))
    if pos:
        i, j = random.choice(pos)
        board[i][j] = 2

# 3. show board
def show():
    for row in board:
        print(row)
    print()

# 4. move LEFT
def move_left():
    for i in range(4):
        row = [x for x in board[i] if x != 0]  # remove zeros

        for j in range(len(row)-1):
            if row[j] == row[j+1]:
                row[j] *= 2
                row[j+1] = 0

        row = [x for x in row if x != 0]        # remove zeros again
        board[i] = row + [0] * (4 - len(row))   # fill with zeros

# start game
add_tile()
add_tile()

while True:
    show()
    choice = input("Press A to move LEFT, Q to quit: ").lower()

    if choice == 'q':
        break
    if choice == 'a':
        move_left()
        add_tile()

