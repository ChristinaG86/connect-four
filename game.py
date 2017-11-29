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
    # y axis needs to be 6 not 7

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
            # checkVertical()
            break
        elif(y == 0):
            print('This column is full! Please try a different column.') 
            print()

currentPlayer = 1
while(True):
    chooseColumn()
    try:
        choiceInt = int(choice) 
    except ValueError: 
        print('You didn\'t enter a number! Please enter a number between 1 and 7.\n')
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
        continue
    printBoard() # don't print when column full

# position = [1, 0]
nextY = position[1] + 1
nextX = position[0] 

if columns[nextY][nextX] == playerToken and columns[nextY + 1][nextX] == playerToken
# keep adding + 2 + 3

# def checkVertical(playerToken, position):
#     if columns[x][0] and columns[y][0] == playerToken:
#         if columns[x][0] and columns[y][1] == playerToken:
#             if columns[x][0] and columns[y][2] == playerToken:
#                 if columns[x][0] and columns[y][3] == playerToken:
#                     print('You won!')
        

