board = [' 'for x  in range(10)]
def insertletter(letter,pos):
    board[pos]=letter
def isfree(pos):
    return board[pos]==' '
def isfull(pos):
    if board.count(' ') > 1:
        return False
    else:
        return True
def printBoard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('~~~~~~~~~~~')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('~~~~~~~~~~~')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
def iswinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l))
def playerMove():
    run=True
    while(run):
        move=input("Enter the position of your move ")
        try:
            move = int(move)
            if move>0 and move<10:
                if isfree(move):
                    run=False
                    insertletter('X',move)
                else:
                    print("Sorry the place is already occupied ")
            else:
                print("Enter the move between 1 and 9")
        except:
            print("Please type a number")
def computerMove():y
    possibleMoves=[x for x,letter in enumerate(board) if letter ==' ' and x!=0]
    move=0
    for let in ['0','X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i]=let
            if iswinner(boardcopy, let):
                move =i;
                return move
    corneropen=[]
    for i in possibleMoves:
        for i in [1,3,7,9]:
            corneropen.append(i) 
    if len(corneropen)>0:
        move = selectRandom(corneropen)
        return move
    
    if 5 in possibleMoves:
        move =5
        return move

    edgeopen = []
    for i in possibleMoves:
        for i in [2,4,6,8]:
            edgeopen.append(i)
    
    if len(edgeopen)>0:
        move = selectRandom(edgeopen)
        return move
def selectRandom(l):
    import random
    length = len(l)
    r = random.randrange(0, length)
    return l[r]
def main():
    print("Welcome to the game !")
    printBoard(board)

    while not(isfull(board)):
        if not(iswinner(board,'0')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you Lose")
            break
        if not(iswinner(board,'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertletter('0',move)
                print("Computer placed an 0 on position ",move ,':')
                printBoard(board)
        else:   
            print("You Win")
            break
    if isfull(board):
        print("Tie  Game ")
while True:
    x= input("Do you want to play again? (y/n)")
    if x.lower()=='y':
        board = [' 'for x  in range(10)]
        print("~~~~~~~~~~~~~~~~~~")
        main()
    else:
        break 