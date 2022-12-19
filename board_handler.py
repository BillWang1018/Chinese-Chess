from init_board import *

__rowSize__, __colSize__ = 2,4

def printBoard(board):

    chess = getDefaultChessDictionary()
    board_line = getDefaultBoardLine()

    # print(type(printBuffer[0]))

    for row in range(10):
        pos = (-1,-1)
        buffer = ''
        for col in range(9):
            pos = (row*__rowSize__, col*__colSize__)
            c = board[row][col]
            if(c != '0'):
                buffer = buffer + chess[c] + ('' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+4])
            else:
                buffer = buffer + (board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+4])
        board_line[pos[0]] = buffer


    print(end="   ")
    for i in range(9):
        print(i+1, ' '*(__colSize__-2), end="")
    print('\n')
    countRow = 0
    resetRow = __rowSize__
    for b in board_line:
        if resetRow == __rowSize__:
            print(chr(97+countRow), end="  ") # 97 = a
            resetRow = 1
            countRow += 1
        else:
            print(end="   ")
            resetRow += 1
        print(b)
        

# test
test = getDefaultBoardData()
printBoard(test)
