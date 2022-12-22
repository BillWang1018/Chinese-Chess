# True: red, False: black
from checkwalk import checkB, checkC, checkK, checkM, checkP, checkS, checkX

def checkValid(turn:bool, startPos:tuple, endPos:tuple, board) -> bool:

    c = board[startPos[0]][startPos[1]]
    e = board[endPos[0]][endPos[1]]

    if(c == '0'):
        raise Exception("You are moving nothing!")

    if(startPos == endPos):
        raise Exception("You are not moving chess!")

    if(turn ^ c.isupper()): # one didn't match --xor>> true
        raise Exception("You cannot move your opponent's chess!")

    if((not (turn ^ e.isupper())) & (e != '0')):
        raise Exception("You cannot kill your own chess!")

    c = c.lower()

    if c == 'b':
        if not checkB(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 'p':
        if not checkP(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 'c':
        if not checkC(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 'm':
        if not checkM(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 'x':
        if not checkX(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 's':
        if not checkS(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")
    if c == 'k':
        if not checkK(startPos, endPos, board):
            raise Exception("You cannot move the chess that way!")

    return True