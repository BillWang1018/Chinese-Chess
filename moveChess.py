from checkValid import checkValid

# constants
__rowSize__, __colSize__ = 2,4

# from a1 to (0, 0)
def strToPosition(str):
    try:
        x = int(ord(str[0])-97)
        y = int(str[1])-1
    except:
        raise Exception("Bad expression!")
    return (x, y)

def moveChess(moveCmd, board, turn):

    try:
        moveCmd = moveCmd.split(" ")
        startPos = strToPosition(moveCmd[0])
        endPos = strToPosition(moveCmd[1])
    except:
        raise Exception("Bad expression!")

    if(startPos[0] == -1 or startPos[1] == -1):
        raise Exception("This coordinate isn't exist!")
    if(endPos[0] == -1 or endPos[1] == -1):
        raise Exception("This coordinate isn't exist!")

    c = board[startPos[0]][startPos[1]]
    
    if(checkValid(c, turn)):
        board[startPos[0]][startPos[1]] = '0'
        board[endPos[0]][endPos[1]] = c
    
    return True
