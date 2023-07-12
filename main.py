import time

ascii_art = open('ascii_art').read()


def check_move(key, my_dict):
    try:
        my_dict[key]
    except KeyError:
        return False
    else:
        return True


def check_winner():
    if board_dict["1"] != " " and board_dict["1"] == board_dict["2"] == board_dict["3"]:
        return True
    if board_dict["1"] != " " and board_dict["1"] == board_dict["4"] == board_dict["7"]:
        return True
    if board_dict["1"] != " " and board_dict["1"] == board_dict["5"] == board_dict["9"]:
        return True
    if board_dict["2"] != " " and board_dict["2"] == board_dict["5"] == board_dict["8"]:
        return True
    if board_dict["3"] != " " and board_dict["3"] == board_dict["6"] == board_dict["9"]:
        return True
    if board_dict["7"] != " " and board_dict["7"] == board_dict["8"] == board_dict["9"]:
        return True
    if board_dict["3"] != " " and board_dict["3"] == board_dict["5"] == board_dict["7"]:
        return True


def check_draw():
    if board_dict["1"] != " " \
            and board_dict["2"] != " " \
            and board_dict["3"] != " " \
            and board_dict["4"] != " " \
            and board_dict["5"] != " " \
            and board_dict["6"] != " " \
            and board_dict["7"] != " " \
            and board_dict["8"] != " " \
            and board_dict["9"] != " ":
        return True


game_on = True
while game_on:
    print(ascii_art)
    time.sleep(1)
    board_dict = {"1": " ",
                  "2": " ",
                  "3": " ",
                  "4": " ",
                  "5": " ",
                  "6": " ",
                  "7": " ",
                  "8": " ",
                  "9": " "}

    print('\n 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n')
    while True:
        move = input('Place X: ')
        valid_move = check_move(move, board_dict)
        while not valid_move:
            print('Choose a number 1-9.')
            move = input('Place X: ')
            valid_move = check_move(move, board_dict)
        while board_dict[move] != " ":
            print('Place X on an empty space.')
            board = f'\n {board_dict["1"]} | {board_dict["2"]} | {board_dict["3"]} ' \
                    f'\n-----------' \
                    f'\n {board_dict["4"]} | {board_dict["5"]} | {board_dict["6"]} ' \
                    f'\n-----------' \
                    f'\n {board_dict["7"]} | {board_dict["8"]} | {board_dict["9"]} \n'
            print(board)
            move = input('Place X: ')
        board_dict[move] = 'X'
        board = f'\n {board_dict["1"]} | {board_dict["2"]} | {board_dict["3"]} ' \
                f'\n-----------' \
                f'\n {board_dict["4"]} | {board_dict["5"]} | {board_dict["6"]} ' \
                f'\n-----------' \
                f'\n {board_dict["7"]} | {board_dict["8"]} | {board_dict["9"]} \n'
        print(board)
        if check_winner():
            print('X Wins!')
            break
        if check_draw():
            print("It's a draw!")
            break
        move = input('Place O: ')
        valid_move = check_move(move, board_dict)
        while not valid_move:
            print('Choose a number 1-9.')
            move = input('Place O: ')
            valid_move = check_move(move, board_dict)
        while board_dict[move] != " ":
            print('Place O on an empty space.')
            board = f'\n {board_dict["1"]} | {board_dict["2"]} | {board_dict["3"]} ' \
                    f'\n-----------' \
                    f'\n {board_dict["4"]} | {board_dict["5"]} | {board_dict["6"]} ' \
                    f'\n-----------' \
                    f'\n {board_dict["7"]} | {board_dict["8"]} | {board_dict["9"]} \n'
            print(board)
            move = input('Place O: ')
        board_dict[move] = 'O'
        board = f'\n {board_dict["1"]} | {board_dict["2"]} | {board_dict["3"]} ' \
                f'\n-----------' \
                f'\n {board_dict["4"]} | {board_dict["5"]} | {board_dict["6"]} ' \
                f'\n-----------' \
                f'\n {board_dict["7"]} | {board_dict["8"]} | {board_dict["9"]} \n'
        print(board)
        if check_winner():
            print('O Wins!')
            break
    if input('\nPlay again? (Y/N): ').upper() == 'Y':
        game_on = True
    else:
        game_on = False
