columns=[[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ']]

print('\nLet\'s play Connect Four!\n') 

def printBoard():
    print(' 1    2    3    4    5    6    7')
    for a in columns:
        print(' ---  ---  ---  ---  ---  ---  ---')
        print('| ' + ' || '.join(a) + ' |')
        print(' ---  ---  ---  ---  ---  ---  ---')
    print()

printBoard() 

def p1choose():
    global p1Choice
    p1Choice = input('Player 1, which column would you like to choose? \n')

p1choose()

while(True):
    try:
        p1ChoiceInt =int(p1Choice) 
    except ValueError: 
        print('You didn\'t enter a number! Please enter a number between 1 and 7.\n')
        p1choose()
        continue
    if p1Choice == "":
        print('You didn\'t enter a number. Please enter a number between 1 and 7.\n')
        p1choose()
        continue
    if p1ChoiceInt >= 1 and p1ChoiceInt <= 7: 
        print('You have chosen column ' + p1Choice)
        break
    else:
        print('There\'s no column ' + p1Choice + '. Please enter a number between 1 and 7.\n') 
        p1choose()
        continue