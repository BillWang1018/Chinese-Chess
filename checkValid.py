
# True: red, False: black
def checkValid(c, turn) -> bool:

    if(c == '0'):
        raise Exception("You're moving an empty chess!")

    if(turn ^ c.isupper()): # one didn't match --xor>> true
        raise Exception("You can't move your opponent's chess!")

    return True

'''

switch-case for every chess
    ...
    ...
    ...

'''
    