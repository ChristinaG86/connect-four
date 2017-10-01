columns=[[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ']]

print('\nLet\'s play Connect Four!\n')

print(' 1    2    3    4    5    6    7')
for a in columns:
    print(' ---  ---  ---  ---  ---  ---  ---')
    print('| ' + ' || '.join(a) + ' |')
    print(' ---  ---  ---  ---  ---  ---  ---')
print()

print('Player 1, your token is O, player two your token is X\n')

p1Choice = input('Player 1, which column would you like to choose? \n')

try:
    p1ChoiceInt =int(p1Choice)
except ValueError:
    print('You didn\'t enter a number!')
    p1ChoiceInt=0

if p1ChoiceInt >= 1 and p1ChoiceInt <= 7:
    print('You have chosen column ' + p1Choice)
else:
    print('There\'s no column ' + p1Choice + '. Please enter a number between 1 and 7.\n')  # Handle what to print when no user input. Loop back to p1Choice input. 

# row = ''
#
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
