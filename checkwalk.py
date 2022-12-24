def checkB(check, walk, board):

    if check[1] == walk[1]:#判斷是否往前後
        if board[check[0]][check[1]] == 'b':#判斷紅方黑方
            if walk[0] == check[0]+1:#判斷是否只走一步
                return True
            return False
        elif board[check[0]][check[1]] == 'B':
            if walk[0] == check[0]-1:
                return True
            return False
        return True
    if abs(walk[1]-check[1]) == 1 and check[0] == walk[0]:#判斷是否往左或右走一步
        if board[check[0]][check[1]] == 'b' and check[0] <= 4:#判斷是否在己方陣地內
            return False
        elif board[check[0]][check[1]] == 'B' and check[0] >= 5:
            return False
        return True
    return False

def checkP(check, walk, board):
    if check[0] == walk[0]:#判斷前後走或左右走
        k1 = min(check[1], walk[1])+1
        k2 = max(check[1], walk[1])
        n = 0
        for k in range(k1, k2):#判斷路徑間是否有其他棋子
            if board[check[0]][k] != '0':
                n += 1
        if k1 == k2:
            n = 0
        if (board[walk[0]][walk[1]] != '0') and n == 1:#判斷是否符合車的吃棋邏輯 即隔山打牛
            return True
        elif (board[walk[0]][walk[1]] == '0') and n == 0:#判斷是否符合砲的移動邏輯 即前後左右走法
            return True
        return False
    if check[1] == walk[1]:
        k1 = min(check[0], walk[0])+1
        k2 = max(check[0], walk[0])
        n = 0
        for k in range(k1, k2):
            if board[k][check[1]] != '0':
                n += 1
        if k1 == k2:
            n = 0
        if (board[walk[0]][walk[1]] != '0') and n == 1:
            return True
        elif (board[walk[0]][walk[1]] == '0') and n == 0:
            return True
        return False
    return False

def checkC(check, walk, board):
    if check[0] == walk[0]:#判斷是否符合車的移動邏輯 即前後左右走法
        k1 = min(check[1], walk[1])+1
        k2 = max(check[1], walk[1])
        for k in range(k1, k2):#判斷路徑間是否有其他棋子
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
    if abs(walk[0]-check[0]) == 2 and abs(walk[1]-check[1]) == 1:#判斷是否符合馬的移動邏輯 即日字走法
        if board[int((check[0]+walk[0])/2)][check[1]] != '0':#判斷路徑間是否存在棋子
            return False
        return True
    elif abs(walk[0]-check[0]) == 1 and abs(walk[1]-check[1]) == 2:
        if board[check[0]][int((check[1]+walk[1])/2)] != '0':
            return False
        return True
    return False

def checkX(check, walk, board):
    if (check[0] <= 4 and walk[0] >= 5) or (walk[0] <= 4 and check[0] >= 5):#判斷是否過河
        return False
    if abs(walk[0]-check[0]) != 2 or abs(walk[1]-check[1]) != 2:#判斷是否符合象的移動邏輯 即田字走法
        return False
    if board[int((check[0]+walk[0])/2)][int((check[1]+walk[1])/2)] != '0':#判斷路徑間是否存在棋子
        return False
    return True

def checkS(check, walk, board):
    if walk[1] < 3 or walk[1] > 5:#判斷是否離開米字九宮格
        return False
    elif walk[0] > 2 and walk[0] < 7:
        return False
    if abs(walk[1]-check[1]) == 1 and abs(walk[0]-check[0]) == 1:#判斷是否符合象的移動邏輯 即口字走法
        return True
    return False

def checkK(check, walk, board):
    if walk[1] < 3 or walk[1] > 5:#判斷是否離開米字九宮格
        return False
    elif walk[0] > 2 and walk[0] < 7:
        return False
    if check[1] == walk[1] and (board[walk[0]][walk[1]] == 'k' or board[walk[0]][walk[1]] == 'K'):#判斷是否王見王
        k1 = min(check[0], walk[0])+1
        k2 = max(check[0], walk[0])
        for k in range(k1, k2):#判斷路徑間是否存在棋子
            if board[k][check[1]] != '0':
                return False
        return True
    if check[0] == walk[0] and abs(walk[1]-check[1]) == 1:#判斷是否符合將帥的移動邏輯 即前後左右走法
        return True
    elif check[1] == walk[1] and abs(walk[0]-check[0]) == 1:
        return True
    return False
