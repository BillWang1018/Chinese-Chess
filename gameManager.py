from moveChess import moveChess
# from drawBoard import drawBoard
from drawBoardWithColor import drawBoardColored
from init_data import getDefaultBoardData
from termcolor import colored
import colorama
import os

def startGame():
    turn = True # True: red, False: black
    boardData = getDefaultBoardData()
    drawBoardColored(boardData)
    colorama.init()

    while(True):

        while(True):

            try: 
                whosTurn = colored("紅", "red") if turn else colored("黑", attrs=["bold"])
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
            
        os.system('cls')
        drawBoardColored(boardData)

        turn = not turn # switch side