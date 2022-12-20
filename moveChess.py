from init_data import getDefaultBoardLine, getDefaultChessDictionary

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
