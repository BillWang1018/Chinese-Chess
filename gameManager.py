from board_handler import *
from init_board import getDefaultBoardData

round = True # True: red, False: black
board = getDefaultBoardData()
printBoard(board)

while(True):
    print("紅方下：" if round else "黑方下：", end="")

    move = input()
    moveCmd = move.split(" ")
    moveChess(moveCmd[0], moveCmd[1], board)

    printBoard(board)

    round = not round