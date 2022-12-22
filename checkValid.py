# True: red, False: black
def checkValid(c:str, turn:bool, startPos:tuple, endPos:tuple) -> bool:

    if(c == '0'):
        raise Exception("You are moving nothing!")

    if(startPos == endPos):
        raise Exception("You are not moving chess!")

    if(turn ^ c.isupper()): # one didn't match --xor>> true
        raise Exception("You cannot move your opponent's chess!")

    c = c.lower()

'''
    if c == 'b':
        
    if c == 'p':

    if c == 'c':

    if c == 'm':

    if c == 'x':

    if c == 's':

    if c == 'k':

    return True

'''
'''
switch-case for every chess
    ...
    'b': '卒',
    'p': '砲',
    'c': '車',
    'm': '馬',
    'x': '象',
    's': '士',
    'k': '將',

'''
    