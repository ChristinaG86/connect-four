columns=[[' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

print('\nLet\'s play Connect Four!\n') 

def printBoard():
    print('  1    2    3    4    5    6    7')
    for y in range(0, len(columns[0])): 
        print(' ---  ---  ---  ---  ---  ---  ---')
        for x in range(0, len(columns)): 
            print('| ', end='')
            print(columns[y][x], end='')
            print(' |', end='')
        print('\n ---  ---  ---  ---  ---  ---  ---')

printBoard() 

print('\nPlayer 1, your token is X. Player 2, your token is O.\n')

def chooseColumn():
    global choice
    prompt = 'Player {}, which column would you like to choose? \n'.format(currentPlayer)
    choice = input(prompt)
    print()

def updateBoard(choice, playerToken):
    # for loop is iterating from bottom of the board to the top
    for y in range(len(columns[0]) -1, -1, -1):
        # placing token in board where space is available
        if columns[y][choice -1] == ' ':
            columns[y][choice -1] = playerToken
            break
        elif(y == 0):
            print('Column is full!') 
            # need to finish this

currentPlayer = 1
while(True):
    chooseColumn()
    try:
        choiceInt = int(choice) 
    except ValueError: 
        print('You didn\'t enter a number! Please enter a number between 1 and 7.\n')
        chooseColumn()
        continue
    if choice == "":
        print('You didn\'t enter a number. Please enter a number between 1 and 7.\n')
        chooseColumn()
        continue
    if choiceInt >= 1 and choiceInt <= 7: 
        print('You have chosen column ' + choice + '\n')
        if currentPlayer == 1:
            playerToken = 'X'
            currentPlayer = 2
        else:
            playerToken = 'O'
            currentPlayer = 1
        updateBoard(choiceInt, playerToken)
    else:
        print('There\'s no column ' + choice + '. Please enter a number between 1 and 7.\n') 
        chooseColumn()
        continue
    printBoard()
