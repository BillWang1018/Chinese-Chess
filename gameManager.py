from moveChess import moveChess
from drawBoard import drawBoard
from init_data import getDefaultBoardData


def startGame():
    round = True # True: red, False: black
    boardData = getDefaultBoardData()
    drawBoard(boardData)

    while(True):

        while(True):
            try: 
                print("紅方下：" if round else "黑方下：", end="")
                move = input()
                moveCmd = move.split(" ")
                valid = moveChess(moveCmd[0], moveCmd[1], boardData)

            except KeyboardInterrupt:
                exit()

            except:
                print("Input error, try again!")

            else:
                break
            
        if(valid):
            drawBoard(boardData)
        else:
            print("This move is illegal!")
            continue

        round = not round # switch side
