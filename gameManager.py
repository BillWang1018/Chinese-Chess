from moveChess import moveChess
from drawBoard import drawBoard
# from drawBoardWithColor import drawBoardColored
from init_data import getDefaultBoardData
from termcolor import colored, cprint
import colorama
import os

boardData = getDefaultBoardData()

def startGame(color:bool=True, autoReverse:bool=False) -> None:

    boardData = getDefaultBoardData()

    turn = True # True: red, False: black

    if (color):
        colorama.init()

    drawBoard(boardData, color, autoReverse&True)

    while(True):

        while(True):

            try: 
                if(color):
                    whosTurn = colored("紅", "red") if turn else colored("黑", attrs=["bold"])
                else:
                    whosTurn = "紅" if turn else "黑"

                print(whosTurn + "方下：", end="")
                moveInput = input().strip()
                iswin = moveChess(moveInput, boardData, turn)

            except KeyboardInterrupt:
                exit()

            except Exception as errmsg:
                print(errmsg)

            except:
                print("Input error, try again!")

            else:
                break

        if iswin:
            drawBoard(boardData, color, autoReverse&turn) 
            endGame(turn)
            exit()
            
        turn = not turn # switch side

        os.system('cls')
        drawBoard(boardData, color, autoReverse&turn) 


def endGame(turn:bool) -> None:
    if turn:
        cprint("RED has won the game!!!", "white", "on_red")
    else:
        cprint("BLACK has won the game!!!", attrs=["bold", "reverse"])