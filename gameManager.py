from moveChess import moveChess
from drawBoard import drawBoard
# from drawBoardWithColor import drawBoardColored
from init_data import getDefaultBoardData
from termcolor import colored
import colorama
import os

def startGame(color:bool=True, autoReverse:bool=False):

    turn = True # True: red, False: black
    boardData = getDefaultBoardData()
    
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
                moveInput = input()
                moveChess(moveInput, boardData, turn)

            except KeyboardInterrupt:
                exit()

            except Exception as errmsg:
                print(errmsg)

            except:
                print("Input error, try again!")

            else:
                break
            
        turn = not turn # switch side

        os.system('cls')
        drawBoard(boardData, color, autoReverse&turn)