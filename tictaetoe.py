theBoard = {'21': ' ', '22': ' ', '23': ' ', '24': ' ', '25': ' ',
            '16': ' ', '17': ' ', '18': ' ', '19': ' ', '20': ' ',
            '11': ' ', '12': ' ', '13': ' ', '14': ' ', '15': ' ',
            '6': ' ', '7': ' ', '8': ' ', '9': ' ', '10': ' ',
            '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['21'] + '|' + board['22'] + '|' + board['23'] + '|' +board['24']+ '|' + board['25'])
    print('-+-+-+-+-')
    print(board['16'] + '|' + board['17'] + '|' + board['18']+ '|' +board['19']+ '|' +board['20'])
    print('-+-+-+-+-')
    print(board['11'] + '|' + board['12'] + '|' + board['13']+ '|' +board['14']+ '|' +board['15'])
    print('-+-+-+-+-')
    print(board['6'] + '|' + board['7'] + '|' + board['8']+ '|' +board['9']+ '|' +board['10'])
    print('-+-+-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3']+ '|' +board['4']+ '|' +board['5'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count >= 5:
            if theBoard['21'] == theBoard['22'] == theBoard['23']== theBoard['24']== theBoard['25'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['16'] == theBoard['17'] == theBoard['18']== theBoard['19']== theBoard['20'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['11'] == theBoard['12'] == theBoard['13']== theBoard['14']== theBoard['15'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['6'] == theBoard['7'] == theBoard['8']== theBoard['9']== theBoard['10'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3']== theBoard['4']== theBoard['5'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['6'] == theBoard['11']== theBoard['16']== theBoard['21'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['7'] == theBoard['12']== theBoard['17']== theBoard['22'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['8'] == theBoard['13']== theBoard['18']== theBoard['23'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['9'] == theBoard['14'] == theBoard['19'] == theBoard['24'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['5'] == theBoard['10'] == theBoard['15'] == theBoard['20'] == theBoard['25'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['21'] == theBoard['17'] == theBoard['13'] == theBoard['9'] == theBoard['5'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['7'] == theBoard['13'] == theBoard['19'] == theBoard['25'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        if count == 25:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()