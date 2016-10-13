import os 
import random

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class bcolors: # colors
    BLUE = '\033[94m' 
    RED = '\033[91m'
    ENDC = '\033[0m'
   
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def drawBoard():
    print("-------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " |")
    print("-------------------")
    print("| ", board[3], " | ", board[4], " | ", board[5], " |")
    print("-------------------")
    print("| ", board[6], " | ", board[7], " | ", board[8], " |")
    print("-------------------")

def emptySpot(player):
    if board[player] != bcolors.BLUE + "X" + bcolors.ENDC and board[player] != bcolors.RED + "O" + bcolors.ENDC:
        return True

def winnerLine(player, spot1, spot2, spot3):
    global board
    if board[spot1] == player and board[spot2] == player and board[spot3] == player:
        return True 

def win(player):
    if winnerLine(player, 0, 1, 2): #horizontal
        return True
    if winnerLine(player, 3, 4, 5):
        return True
    if winnerLine(player, 6, 7, 8):
        return True

    if winnerLine(player, 0, 3, 6): #vertical
        return True
    if winnerLine(player, 1, 4, 7):
        return True
    if winnerLine(player, 2, 5, 8):
        return True
        
    if winnerLine(player, 0, 4, 8): #diagonal
        return True
    if winnerLine(player, 2, 4, 6):
        return True

def fullBoard():
    global board
    count = 0
    for i in range(9):
        if board[i] == bcolors.BLUE + "X" + bcolors.ENDC or board[i] == bcolors.RED + "O" + bcolors.ENDC:
            count = count + 1
        if count == 9:
            return True 

def playAgain():
    while True:
        global board
        yes_or_no = input("Do you want to play again? (y or n) ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if yes_or_no == "y":
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            drawBoard()
            break
        else:
            exit()

def playAgainstCom():
    global name2
    if name2 == "C" or name2 == "c":
        return True      

wins_name1 = 0  # number of wins of player1
wins_name2 = 0  # number of wins of player2

def numberOfWins1(name): # player1
    global wins_name1
    wins_name1 = wins_name1 + 1
    print(name + " has " + str(wins_name1) + " win(s).")

def numberOfWins2(name): # player2
    global wins_name2
    wins_name2 = wins_name2 + 1
    print(name + " has " + str(wins_name2) + " win(s).")
        
#HERE STARTS THE GAME
clearTerminal()
print("Welcome to Tic Tac Toe!")
print("Get ready for an awesome experience!", "\n")

name1 = input("Player1, what's your name? ")
if name1 == "": 
    name1 = "Player1" # if no name is given, it will be Player1
name1 = bcolors.BLUE + name1 + bcolors.ENDC

name2 = input("Player2, what's your name? (Type in C to play against Computer) ")
if name2 != "C" and name2 != "c": # play against human
    if name2 == "":
        name2 = "Player2" # if no name is given, it will be Player2
    name2 = bcolors.RED + name2 + bcolors.ENDC   

clearTerminal()

drawBoard()

if not playAgainstCom(): #play against human
    while True:  
        
        while True:
            player1 = input( name1 + ", select a spot(1-9): ")
            if player1.isdigit():
                player1 = int(player1)
                player1 = player1 - 1
                if player1 > 8:
                    print("Select a spot between 1 and 9!")
                else:
                    break
                
        if emptySpot(player1):
            board[player1] = bcolors.BLUE + "X" + bcolors.ENDC

            clearTerminal()

            drawBoard()

            if win(bcolors.BLUE + "X" + bcolors.ENDC):
                print(name1 + " wins!")
                numberOfWins1(name1)
                if playAgainstCom():
                    print(bcolors.RED + "Computer" + bcolors.ENDC + " has " + str(wins_name2) + " win(s).")
                else:
                    print(name2 + " has " + str(wins_name2) + " win(s).")
                playAgain()

            if fullBoard() is True:
                print("It's a draw!")
                playAgain()      

            while True and not fullBoard():

                while True:
                    player2 = input( name2 + ", select a spot(1-9): ")
                    if player2.isdigit():
                        player2 = int(player2)
                        player2 = player2 - 1
                        if player2 > 8:
                            print("Select a spot between 1 and 9!")
                        else:
                            break

                if emptySpot(player2):
                    board[player2] = bcolors.RED + "O" + bcolors.ENDC

                    clearTerminal()

                    drawBoard()

                    if win(bcolors.RED + "O" + bcolors.ENDC):
                        print(name2 +" wins!")
                        numberOfWins2(name2)
                        print(name1 + " has " + str(wins_name1) + " win(s).")
                        playAgain() 
                
                    if fullBoard() is True:
                        print("It's a draw!")
                        playAgain()
                  
                    break 

                else:
                    print("Choose another spot!")

        else:
            print("Choose another spot!")

else: #play against computer
    while True:  
        
        while True:
            player1 = input( name1 + ", select a spot(1-9): ")
            if player1.isdigit():
                player1 = int(player1)
                player1 = player1 - 1
                if player1 > 8:
                    print("Select a spot between 1 and 9!")
                else:
                    break
                
        if emptySpot(player1):
            board[player1] = bcolors.BLUE + "X" + bcolors.ENDC

            clearTerminal()

            drawBoard()

            if win(bcolors.BLUE + "X" + bcolors.ENDC):
                print(name1 + " wins!")
                numberOfWins1(name1)
                if playAgainstCom():
                    print(bcolors.RED + "Computer" + bcolors.ENDC + " has " + str(wins_name2) + " win(s).")
                else:
                    print(name2 + " has " + str(wins_name2) + " win(s).")
                playAgain()

            if fullBoard() is True:
                print("It's a draw!")
                playAgain()      

            while True and not fullBoard():
         
                name2 = bcolors.RED + "Computer" + bcolors.ENDC

                random.seed
                player2 = random.randrange(0, 9)
                
                if emptySpot(player2):
                    board[player2] = bcolors.RED + "O" + bcolors.ENDC

                    clearTerminal()   

                    drawBoard()

                    if win(bcolors.RED + "O" + bcolors.ENDC):
                        print(name2 +" wins!")
                        numberOfWins2(name2)
                        print(name1 + " has " + str(wins_name1) + " win(s).")
                        playAgain()

                    if fullBoard() is True:
                        print("It's a draw!")
                        playAgain()
                        
                    break                             
                
        else:
            print("Choose another spot!")
    

    