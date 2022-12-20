from init_board import getDefaultBoardLine, getDefaultChessDictionary

# constants
__rowSize__, __colSize__ = 2,4

# from a1 to (0, 0)
def strToPosition(str):
    x = int(ord(str[0])-97)
    y = int(str[1])-1
    if(x < 0 or x >= 10):
        x = -1
    if(y < 0 or y >= 9):
        y = -1
    return (x, y)

def moveChess(start, end, board):

    startPos = strToPosition(start)
    endPos = strToPosition(end)

    if(startPos[0] == -1 or startPos[1] == -1):
        return False
    if(endPos[0] == -1 or endPos[1] == -1):
        return False

    c = board[startPos[0]][startPos[1]]
    board[startPos[0]][startPos[1]] = '0'
    board[endPos[0]][endPos[1]] = c
    
    return True
    
# print the chess board in format
def printBoard(board):
    board_line = getDefaultBoardLine()
    for bl in board_line:
        print(bl)
    chess = getDefaultChessDictionary()
    # modify the output with chess 
    pos = (-1,-1)
    bufferList = []
    for row in range(10):
        buffer = ''
        for col in range(9):
            pos = (row*__rowSize__, col*__colSize__)
            c = board[row][col]
            print(board_line[pos[0]])
            if(c != '0'):
                print(c, pos[0], pos[1], pos[1]+__colSize__, chess[c]+('' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+__colSize__]))

                buffer = buffer + chess[c] + ('' if col==8 else board_line[pos[0]][pos[1]+2:pos[1]+__colSize__])
            else:
                print(c, pos[0], pos[1], pos[1]+__colSize__, board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+__colSize__])

                buffer = buffer + (board_line[pos[0]][pos[1]] if col==8 else board_line[pos[0]][pos[1]:pos[1]+__colSize__])
        
        for i in range(__rowSize__):
            if i == 0:
                bufferList.append(buffer)
            elif col != 9:
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


# test = getDefaultBoardData()
# printBoard(test)
