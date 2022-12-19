from init_board import *

# constants
__rowSize__, __colSize__ = 2,4
chess = getDefaultChessDictionary()
board_line = getDefaultBoardLine()

# from a1 to (0, 0)
def strToPosition(str):
    return (int(ord(str[0])-97), int(str[1])-1)

def moveChess(start, end, board):

    startPos = strToPosition(start)
    endPos = strToPosition(end)

    print(startPos, endPos)

    c = board[startPos[0]][startPos[1]]
    board[startPos[0]][startPos[1]] = '0'
    board[endPos[0]][endPos[1]] = c
    
    return board
    
# print the chess board in format
def printBoard(board):

    # modify the output with chess 

    pos = (-1,-1)
    for row in range(10):
        buffer = ''
        for col in range(9):
            pos = (row*__rowSize__, col*__colSize__)
            c = board[row][col]
            print(row, col)
            if(c != '0'):
                buffer = buffer + chess[c] + ('' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+4])
            else:
                buffer = buffer + (board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+4])
        board_line[pos[0]] = buffer

    # print out the chess board
    # print 1-9
    print(end="   ")
    for i in range(9): 
        print(i+1, ' '*(__colSize__-2), end="")
    print()

    # print a-j ahead every row
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
        
    print(end="   ")
    for i in range(9): 
        print(i+1, ' '*(__colSize__-2), end="")
    print('\n')

# test
# test = getDefaultBoardData()
# printBoard(test)
