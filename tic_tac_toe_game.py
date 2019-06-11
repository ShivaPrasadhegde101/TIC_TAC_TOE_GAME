
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
check=1
win=1
tie=-1
running=0
game=running
chance='X'

#function to draw the board
def Draw():
    print("%c  | %c |%c"%(board[1],board[2],board[3]))
    print("___|___|___")
    print("%c  | %c |%c"%(board[4],board[5],board[6]))
    print("___|___|___")
    print("%c  | %c |%c"%(board[7],board[8],board[9]))
    print("   |   |   ")

#function to check if the entered position is empty or not

def Check(x):
    if(board[x]==' '):
        return True
    else:
        return False
        print("Already filled try again please")

#function to check who won or whether its a draw
def Winner():
    global game
    if(board[1]==board[2] and board[2] ==board[3] and board[2]!=' '):
        game=win
    elif(board[4]==board[5] and board[5] ==board[6] and board[5]!=' '):
        game=win
    elif(board[7]==board[8] and board[8] ==board[9] and board[8]!=' '):
        game=win
    elif(board[1]==board[4] and board[4] ==board[7] and board[1]!=' '):
        game=win
    elif(board[2]==board[5] and board[5] ==board[8] and board[2]!=' '):
        game=win
    elif(board[3]==board[6] and board[6] ==board[9] and board[3]!=' '):
        game=win
    elif(board[1]==board[5] and board[5] ==board[9] and board[5]!=' '):
        game=win
    elif(board[3]==board[5] and board[5] ==board[7] and board[5]!=' '):
        game=win
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game=tie
    else:
        game=running
        
def Game():
    global check
    global game
    global board
    global win
    global tie
    global running
    global chance
    print()
    while(game==running):
        Draw()
        if(check%2!=0):
            print("Player1 chance")
            chance='X'
        else:
            print("Player2 chance")
            chance='O'
        n=input("Enter the position [1-9]:")
        n=int(n)
        if(n>=1 and n<=9):
            if(Check(n)):
                board[n]=chance
                check+=1
                Winner()
        else:
            print("Enter valid numbers")
            print()

    Draw()
    if(game==tie):
        print("Game tie")
    elif(game==win):
        if(check%2==0):
            print("Player1 won")
        else:
            print("Player2 won")

    re=input("Do you want to play again(y/n):")
    if(re=='y'):
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        check=1
        win=1
        tie=-1
        running=0
        game=running
        chance='X'
        Game()
    else:
        quit()

Game()
