def checkB(check, walk, board):

    if check[1] == walk[1] and walk[0] == check[0]+1:
        return True
    if abs(walk[1]-check[1]) == 1 and check[0] == walk[0]:
        if board[check[0]][check[1]] == 'b' and check[0] <= 4:
            return False
        elif board[check[0]][check[1]] == 'B' and check[0] >= 5:
            return False
        return True
    return False

def checkP(check, walk, board):
    if check[0] == walk[0]:
        k1 = min(check[1], walk[1])+1
        k2 = max(check[1], walk[1])
        for k in range(k1, k2):
            if board[check[0]][k] != '0':
                if board[walk[0]][walk[1]] != '0':
                    return True
                return False
        return True
    if check[1] == walk[1]:
        k1 = min(check[0], walk[0])+1
        k2 = max(check[0], walk[0])
        for k in range(k1, k2):
            if board[k][check[1]] != '0':
                if board[walk[0]][walk[1]] != '0':
                    return True
                return False
        return True
    else:
        return False

def checkC(check, walk, board):
    if check[0] == walk[0]:
        k1 = min(check[1], walk[1])+1
        k2 = max(check[1], walk[1])
        for k in range(k1, k2):
            if board[check[0]][k] != '0':
                return False
        return True
    if check[1] == walk[1]:
        k1 = min(check[0], walk[0])+1
        k2 = max(check[0], walk[0])
        for k in range(k1, k2):
            if board[k][check[1]] != '0':
                return False
        return True
    return False

def checkM(check, walk, board):
    if abs(walk[0]-check[0]) == 2 and abs(walk[1]-check[1]) == 1:
        if board[(check[0]+walk[0])/2][check[1]] != '0':
            return False
        return True
    elif abs(walk[0]-check[0]) == 1 and abs(walk[1]-check[1]) == 2:
        if board[check[0]][(check[1]+walk[1])/2] != '0':
            return False
        return True
    return False

def checkX(check, walk, board):
    if check[0] <= 4 and walk[0] >= 5 or walk[0] <= 4 and check[0] >= 5:
        return False
    if abs(walk[0]-check[0]) != 2 or abs(walk[1]-check[1]) != 2:
        return False
    if board[(check[0]+walk[0])/2][(check[1]+walk[1])/2] != '0':
        return False
    return True

def checkS(check, walk, board):
    if walk[1] < 3 and walk[1] > 5:
        return False
    elif walk[0] > 2 and walk[0] < 7:
        return False
    if check[0] == walk[0] and abs(walk[1]-check[1]) == 1:
        return True
    elif check[1] == walk[1] and abs(walk[0]-check[0]) == 1:
        return True
    return False

def checkK(check, walk, board):
    if walk[1] < 3 and walk[1] > 5:
        return False
    elif walk[0] > 2 and walk[0] < 7:
        return False
    elif abs(walk[1]-check[1]) == 1 and abs(walk[0]-check[0]) == 1:
        return True
    return False