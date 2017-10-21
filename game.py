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





# invalidInput = True
# while(invalidInput): 
#     try:
#         p1ChoiceInt =int(p1Choice) # check if user input is a number 
#     except ValueError: # print error if not 
#         print('You didn\'t enter a number!')
#         p1choose() # and call p1choose function again
#         # need something here to say 'begin loop again'
#     if p1Choice == "": # check if user enters an empty string
#         print('You didn\'t enter a number. Please enter a number between 1 and 7.\n')
#         p1choose() # call p1choose function again
#         # loop again
#     if p1ChoiceInt >= 1 and p1ChoiceInt <= 7:
#         print('You have chosen column ' + p1Choice)
#         break
#     else:
#         print('There\'s no column ' + p1Choice + '. Please enter a number between 1 and 7.\n') 
#         invalidInput = p1Choice == "" or (p1ChoiceInt < 1 and p1ChoiceInt > 7) 
#         p1choose()  
        # loop again                                          

# if user enters valid input, add token to selected column array




# print('Player 1, your token is O, player two your token is X\n')

# if p1Choice is None:
#     print('You didn\'t enter a number!')

# row =
# for i in range(len(columns)):
# #     for row = row + x
#       x in columns[i]:
# #

# print(' ---  ---  ---  ---')
# print('| ' + row[4] + ' |' + '| ' + row[5] + ' |' + '| ' + row[6] + ' |' + '| ' + row[7] + ' |')
# print(' ---  ---  ---  ---')
# print(' ---  ---  ---  ---')
# print('| ' + row[8] + ' |' + '| ' + row[9] + ' |' + '| ' + row[10] + ' |' + '| ' + row[11] + ' |')
# print(' ---  ---  ---  ---')
# print(' ---  ---  ---  ---')
# print('| ' + row[12] + ' |' + '| ' + row[13] + ' |' + '| ' + row[14] + ' |' + '| ' + row[15] + ' |')
# print(' ---  ---  ---  ---')

# for i, c in enumerate(columns): #i = index of columns list, c = whole row
#     for x, y in enumerate(c): #x=index of inside row, y= value within row
#         print(i, x, y)
#         print('| ' + row[0] + ' |' + '| ' + row[1] + ' |' + '| ' + row[2] + ' |' + '| ' + row[3] + ' |')

# for i in range(len(columns)):
#     for j in range(len(columns[i])):
#         print(columns[i][j])

# rows = []
# for x in columns:
#     rows = rows + x
#
# print(rows)

# for x in range(4):
#     print('----  ----  ----  ----')
#     print('|  |  |  |  |  |  |  |')
#     print('----  ----  ----  ----')

# for i in row:
#     print(' --- ')
#     print('| ' + i + ' |')
#     print(' ---')

# print(' --- ')
# print('| ' + x + ' |')
# print(' ---')

# print(' --- ')
# print('| ' + columns[0][2] + ' |')
# print(' ---')
#
# print(' --- ')
# print('| ' + columns[0][3] + ' |')
# print(' ---')

# print(columns[0][0], columns[1][0])
# print(columns[0][1], columns[1][1])
# print(columns[0][2], columns[1][2])
# print(columns[0][3], columns[1][3])
