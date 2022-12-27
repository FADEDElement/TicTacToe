import os
import re
import random

def displayBoard():
    os.system("clear")

    print(f"""
         {awnsers[0]} | {awnsers[1]} | {awnsers[2]}
        ---+---+---
         {awnsers[3]} | {awnsers[4]} | {awnsers[5]}
        ---+---+---
         {awnsers[6]} | {awnsers[7]} | {awnsers[8]}
    """)

def gameStart():
    global playing
    global turn
    global awnsers

    playing = True
    turn = "X"
    awnsers = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

    displayBoard()

def translateLocation (location):
    if location == "tl": return 0
    elif location == "tm": return 1
    elif location == "tr": return 2
    elif location == "ml": return 3
    elif location == "m": return 4
    elif location == "mr": return 5
    elif location == "bl": return 6
    elif location == "bm": return 7
    elif location == "br": return 8
    else: return -1

def gameState(awnsersTemp):
    global playing

    temp = " "
    winner = ""
    players = ["X", "O"]
    awnsersTemp = temp.join(awnsersTemp).replace(" ", "")

    for player in players:
        if (re.match(f"{player}{player}{player}[\S][\S][\S][\S][\S][\S]", awnsersTemp) or
            re.match(f"[\S][\S][\S]{player}{player}{player}[\S][\S][\S]", awnsersTemp) or
            re.match(f"[\S][\S][\S][\S][\S][\S]{player}{player}{player}", awnsersTemp) or
            re.match(f"{player}[\S][\S]{player}[\S][\S]{player}[\S][\S]", awnsersTemp) or
            re.match(f"[\S]{player}[\S][\S]{player}[\S][\S]{player}[\S]", awnsersTemp) or
            re.match(f"[\S][\S]{player}[\S][\S]{player}[\S][\S]{player}", awnsersTemp) or
            re.match(f"{player}[\S][\S][\S]{player}[\S][\S][\S]{player}", awnsersTemp) or
            re.match(f"[\S][\S]{player}[\S]{player}[\S]{player}[\S][\S]", awnsersTemp)
        ): winner = player
        elif "-" not in awnsersTemp: winner = "null"

        if winner == player:
            if not input (player + ", congradulations you win!\nWould you like to play again? [y/n] ") == ("y" or "Y"): playing = False
        elif winner == "null":
            if not input ("Draw!\nWould you like to play again? [y/n] ") == ("y" or "Y"): playing = False

        if not playing:
            os.system("clear")
            exit()
        elif not winner == "":
            gameStart()

gameStart()

while playing:
    playablePosition = input(f"{turn} -> Please enter a location: ")

    if translateLocation(playablePosition) == -1 or not awnsers[translateLocation(playablePosition)] == "-":
        displayBoard()
        continue

    awnsers[translateLocation(playablePosition)] = turn
    
    if turn == "X": turn = "O"
    elif turn == "O": turn = "X"

    displayBoard()
    gameState(awnsers)