from init_data import getDefaultBoardLine, getDefaultChessDictionary
from termcolor import colored
import colorama

# constants
__rowSize__, __colSize__ = 2,4
board_line = getDefaultBoardLine()
chess = getDefaultChessDictionary()

# print the chess board in format
def drawBoard(board, color=True, reverse=False):

    if color:
        colorama.init()

    # modify the output with chess 
    pos = (-1,-1)
    bufferList = []

    buffer=' ' * (__rowSize__+1)
    for i in range(9): 
        buffer += (str(i+1) + ' '*(__colSize__-1))
    bufferList.append(buffer)
    # bufferList.append('')

    for row in range(10):
        buffer = (chr(97+row) + ' '*__rowSize__)

        for col in range(9):
            pos = (row*__rowSize__, col*__colSize__)
            c = board[row][col]

            if(c != '0'):
                if color:
                    if(c.isupper()):
                        buffer += colored(chess[c], "white", "on_red")
                    if(c.islower()):
                        buffer += colored(chess[c], "white", attrs=["reverse", "bold"])
                else:
                    buffer += chess[c]
                buffer += '' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+__colSize__]


            else:
                buffer += (board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+__colSize__])
        
        for i in range(__rowSize__):

            if i == 0:
                bufferList.append(buffer)

            elif row != 9:
                bufferList.append(' '*(__rowSize__+1) + board_line[pos[0]+i])


    # bufferList.append('')
    buffer=' ' * (__rowSize__+1)
    for i in range(9): 
        buffer += (str(i+1) + ' '*(__colSize__-1))
    bufferList.append(buffer)
            
    # print out the chess board
    for b in bufferList:
        print(b)

    print()