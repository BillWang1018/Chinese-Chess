from board_handler import printBoard, moveChess
from init_board import getDefaultBoardData

round = True # True: red, False: black
boardData = getDefaultBoardData()
printBoard(boardData)

while(True):
    print("紅方下：" if round else "黑方下：", end="")

    move = input()
    moveCmd = move.split(" ")
    valid = moveChess(moveCmd[0], moveCmd[1], boardData)

    if(valid):
        printBoard(boardData)
    else:
        print("This move is illegal!")
        continue


    round = not round # switch side
