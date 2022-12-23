from checkValid import checkValid
import re

# constants
__rowSize__, __colSize__ = 2,4

# from a1 to (0, 0)
def strToPosition(str:str) -> tuple:
    x = int(ord(str[0])-97)
    y = int(str[1])-1
    return (x, y)

def moveChess(moveCmd:str, board, turn:bool) -> bool:

    if(re.search("^[a-j][1-9]\\s[a-j][1-9]$", moveCmd)):
        moveCmd = moveCmd.split(" ")
        startPos = strToPosition(moveCmd[0])
        endPos = strToPosition(moveCmd[1])
    else:
        raise Exception("Bad expression!")

    c = board[startPos[0]][startPos[1]]
    
    if(checkValid(turn, startPos, endPos, board)):
        if(board[endPos[0]][endPos[1]].lower() == 'k'):
            win = True
        else :
            win = False
        board[startPos[0]][startPos[1]] = '0'
        board[endPos[0]][endPos[1]] = c

        return win
        
    else:
        raise Exception("Not avalible!")
