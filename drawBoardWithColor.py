from init_data import getDefaultBoardLine, getDefaultChessDictionary, getDefaultBoardData
from termcolor import colored, cprint

# constants
__rowSize__, __colSize__ = 2,4
board_line = getDefaultBoardLine()
chess = getDefaultChessDictionary()

# print the chess board in format
def drawBoardColored(board):
    # modify the output with chess 
    pos = (-1,-1)
    bufferList = []

    for row in range(10):
        buffer = ''

        for col in range(9):
            pos = (row*__rowSize__, col*__colSize__)
            c = board[row][col]

            if(c != '0'):
                if(c.isupper()):
                    buffer += colored(chess[c], "white", "on_red")
                if(c.islower()):
                    buffer += colored(chess[c], "white", attrs=["reverse", "bold"])

                    
                buffer += ('' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+__colSize__])

            else:
                buffer += colored(board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+__colSize__])
        
        for i in range(__rowSize__):

            if i == 0:
                bufferList.append(buffer)

            elif row != 9:
                bufferList.append(board_line[pos[0]+i])
            
    # print out the chess board
    # print 1-9
    print(end="   ")

    for i in range(9): 
        print(i+1, ' '*(__colSize__-2), end="")

    print()

    # print a-j ahead every row
    countRow = 0
    resetRow = __rowSize__

    for b in bufferList:

        if resetRow == __rowSize__:
            print(chr(97+countRow), end="  ") # 97 = a
            resetRow = 1
            countRow += 1

        else:
            print(end="   ")
            resetRow += 1

        print(b)
        
    print(end="   ")

    for i in range(9): 
        print(i+1, ' '*(__colSize__-2), end="")

    print('\n')
