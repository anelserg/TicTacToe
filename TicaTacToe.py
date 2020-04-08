n = 3
board = [['-']*n for x in range(n)]

#dictionary to translate from location to coordinates
boardNames={'A1': [0,0],
            'B1': [0,1],
            'C1': [0,2],
            'A2': [1,0],
            'B2': [1,1],
            'C2': [1,2],
            'A3': [2,0],
            'B3': [2,1],
            'C3': [2,2]}

def printBoard():
    # print(board[0][0] + ' ' + board[0][1] + ' ' + board[0][2])
    # print(board[1][0] + ' ' + board[1][1] + ' ' + board[1][2])
    # print(board[2][0] + ' ' + board[2][1] + ' ' + board[2][2])

    print('A1(' + board[0][0] + ') B1(' + board[0][1] + ') C1(' + board[0][2] + ')')
    print('A2(' + board[1][0] + ') B2(' + board[1][1] + ') C2(' + board[1][2] + ')')
    print('A3(' + board[2][0] + ') B3(' + board[2][1] + ') C3(' + board[2][2] + ')')
    

# def printBoardLocations():
#     print('A1 B1 C1')
#     print('A2 B2 C2')
#     print('A3 B3 C3')


def setLocation(location, player):
    # print('parameters: ' + location +' '+ player)
    coordinates = boardNames[location]
    # print('row: ' + str(coordinates[0]))
    # print('column: ' + str(coordinates[1]))
    row = coordinates[0]
    column = coordinates[1]
    board[row][column] = player

def getLocation(location):
    # print('parameters: ' + location)
    coordinates = boardNames[location]
    # print('row: ' + str(coordinates[0]))
    # print('column: ' + str(coordinates[1]))
    row = coordinates[0]
    column = coordinates[1]
    return board[row][column]


currentPlayer = "X"
winner = ''
totalTurns = 0

while True:
    printBoard()
    print("Current player: " + currentPlayer)

    position = input( "Choose a position: " )
    print( position )

    # Valdiating position exists
    if position not in boardNames:
        print("Position " + position + " does not exist!!")
        continue
    
    # Validating the position is available
    if getLocation(position) != "-":
        print("Position " + position + " already taken!!")
        continue

    # Apply the move
    setLocation(position, currentPlayer)
    totalTurns += 1


    # Check if anyone won or tie (no more spaces and no winner)

    for player in ['X', 'O']:
        # checking by rows
        for j in range(3):
            matchCounter = 0
            for i in range(3):
                if board[j][i] == player:
                    matchCounter += 1

            if matchCounter == 3:
                winner = player
                break

        if winner == player:
            break

        # checking by columns
        for i in range(3):
            matchCounter = 0
            for j in range(3):
                if board[j][i] == player:
                    matchCounter += 1

            if matchCounter == 3:
                winner = player
                break

        if winner == player:
            break

        # checking for diagonals
        if board[0][0] == board[1][1] == board[2][2] == player:
            winner = player
            break

        if board[0][2] == board[1][1] == board[2][0] == player:
            winner = player
            break

    if winner != '':
        print(winner, ' is the winner')
        printBoard()
        break

    if winner == '' and totalTurns == 9:
        printBoard()
        print('Game ends in a tie')
        break


    # Switch player turn
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

