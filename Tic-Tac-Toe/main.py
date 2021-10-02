# creating a Dictionary
the_board = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(the_board)
        print(f"{turn} it's your turn move to the place where the field is empty")

        move = input("Enter the Place you want to keep: ")

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['7'] == the_board['8'] == the_board['9'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['3'] == the_board['5'] == the_board['7'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
                print("Game Over")
                print_board(the_board)
                print(f"The winner of this round is {turn}")
                break

            else:
                print("Something is Wrong")

        if count == 9:
            print("The Game has been Tied")
            print_board(the_board)

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    restart_game = input("Do you want to play again, if Yes type 'Y' or type 'N' for No: ")
    if restart_game == 'Y' or restart_game == 'y':
        for keys in board_keys:
            the_board[keys] = ' '
        game()
    else:
        print("Thank You for playing the game")


if __name__ == '__main__':
    game()


