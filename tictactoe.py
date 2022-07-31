import numpy as np 
def PrintRed(char):
    print("\033[91m{}\033[00m" .format(char), end="", sep="") 
def PrintLightBlue(char):
    print("\033[96m{}\033[00m" .format(char), end="", sep="") 
def printInitScreen():
    logo = """
    888   d8b        888                   888
    888   Y8P        888                   888
    888              888                   888
    888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
    888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
    888   888888     888   .d888888888     888   888  88888888888
    Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
     "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888
    """
    print(logo)
def PrintBoard(Board):
    for i in range(9):
        if i % 3 == 0:
            print("         |     |     ")
        if i % 3 == 1:
            for j in range(3):
                curr_index = j + 3*int(i/3)
                if j == 0:
                    print("      ", end="", sep="")
                if Board[curr_index] == 'x':        
                    PrintRed(Board[curr_index])          
                elif Board[curr_index] == 'o':
                    PrintLightBlue(Board[curr_index])
                else:
                    print(Board[curr_index], end="", sep="")
                if j != 2:
                        print("  |  ", end="", sep="")
                
        if i % 3 == 2 and i != 8 :
            print("\n    _____|_____|_____")
        if i == 8:
            print()
            print()
def CheckWin(Board):
    GameWon = False
    if Board[0] == "x" and Board[1] == "x" and Board[2] == "x" or Board[0] == "o" and Board[1] == "o" and Board[2] == "o":
        GameWon = True
    elif Board[0] == "x" and Board[3] == "x" and Board[6] == "x" or Board[0] == "o" and Board[3] == "o" and Board[6] == "o":
        GameWon = True
    elif Board[0] == "x" and Board[4] == "x" and Board[8] == "x" or Board[0] == "o" and Board[4] == "o" and Board[8] == "o":
        GameWon = True
    elif Board[1] == "x" and Board[4] == "x" and Board[7] == "x" or Board[1] == "o" and Board[4] == "o" and Board[7] == "o":
        GameWon = True
    elif Board[2] == "x" and Board[5] == "x" and Board[8] == "x" or Board[2] == "o" and Board[5] == "o" and Board[8] == "o":
        GameWon = True
    elif Board[2] == "x" and Board[4] == "x" and Board[6] == "x" or Board[2] == "o" and Board[4] == "o" and Board[6] == "o":
        GameWon = True
    elif Board[3] == "x" and Board[4] == "x" and Board[5] == "x" or Board[3] == "o" and Board[4] == "o" and Board[5] == "o":
        GameWon = True
    elif Board[6] == "x" and Board[7] == "x" and Board[8] == "x" or Board[6] == "o" and Board[7] == "o" and Board[8] == "o":
        GameWon = True
    return GameWon
def ValidInputBoard(temp,board):
    validinput = False
    if (ord(temp) > 48 and ord(temp) < 58) and (len(temp) == 1) and (not(ord(temp) == 32)) and not(board[int(temp)-1] == 'x' or board[int(temp)-1] == 'o' ) :
        validinput = True  
    return validinput   
def TwoPlayer(Board):
    counter = 0 
    namep1 = input("player 1 enter your name: \n")
    namep2 = input("player 2 enter your name: \n")
    player1 = input("%s yould you like to be x or o ? \n"%namep1)
    while not(player1 == 'x' or player1 == 'o'):
        print("wrong input. enter x or o to play")
        player1 = input("%s yould you like to be x or o ? \n"%namep1)
    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x' 
    print(" %s, you are %s. %s, you are %s. "%(namep1,player1,namep2,player2))  
    for i in range(len(Board)):     
        PrintBoard(Board)   
        temp = input(" %s, pick were you want to put your %s \n"%(namep1,player1))
        while ValidInputBoard(temp,Board) == False:
            print("wrong input.")
            temp = input(" %s, pick were you want to put your %s \n"%(namep1,player1))  
        Board[int(temp)-1] = player1
        PrintBoard(Board)
        counter += 1
        if CheckWin(Board) == True:
            print("%s, you win!!! " %namep1)
            break    
        temp = input("%s, pick were you want to put your %s \n"%(namep2,player2))
        while ValidInputBoard(temp,Board) == False:
            print("wrong input.")
            temp = input(" %s, pick were you want to put your %s \n"%(namep2,player2))  
        Board[int(temp)-1] = player2
        counter += 1
        if CheckWin(Board) == True:
            print("%s, you win!!!" %namep2)
            break
        if counter == 9:
            print("it is a tie!!!")
            break
def Main():
    Board = np.array(['1','2','3','4','5','6','7','8','9'])
    printInitScreen()
    TwoPlayer(Board)
Main()   