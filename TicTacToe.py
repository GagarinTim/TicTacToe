the_row = [
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['___', "|", '___', '|', '___']],
    '\n',
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['___', "|", '___', '|', '___']],
    '\n',
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   ']]]

player1 = ""
player2 = ""
player1_dict = {'symbol': None, 'victories': 0, 'moves': []}
player2_dict = {'symbol': None, 'victories': 0, 'moves': []}
currently_moving_X = True
currently_moving_symbol = 'X'
game_on = True
winner = False
introduce_players = True
n = 0
q2 = ''
q2_bool = False


def switch():
    """
this function as well as used variables allow for flow control
and for announcing who is going to move next
    """
    global currently_moving_symbol
    global currently_moving_X
    if currently_moving_symbol == "X":
        currently_moving_symbol = "O"
    elif currently_moving_symbol == "O":
        currently_moving_symbol = "X"
    if currently_moving_X is True:
        currently_moving_X = False
    elif currently_moving_X is False:
        currently_moving_X = True


def display(the_row):
    print()
    print()
    print()
    for item in the_row:
        for item1 in item:
            for item2 in item1:
                print(item2, end="")
    print()
    print()
    print()


def user_initial_input():
    global player1
    global player2
    player1 = input("Please enter name of player 1: ")
    print("Hello " + player1)
    player2 = input("Please enter name of player 2: ")
    print("Hello " + player2)
    return player1, player2


def user_history():
    global player1_dict
    global player2_dict

    q1 = input(f"Would {player1} like to play as X? 'Y' or 'N': ")
    q1 = q1.lower()
    if q1 != "y" and q1 != "n":
        while q1 != "y" and q1 != "n":
            q1 = input().lower()
            print(
                f"I am not sure I understand. Let's try again. Would {player1} like to play as 'x'? Please answer with 'Y' for 'yes' and 'N' for 'No'.")
    elif q1 == 'y':
        player1_dict['symbol'] = "X"
        player2_dict['symbol'] = "O"
    elif q1 == 'n':
        player1_dict['symbol'] = "O"
        player2_dict['symbol'] = "X"


def move(currently_moving_symbol):
    # function that will alternate variables on the board after accepting user input and changes
    global the_row
    global player1_dict
    global player2_dict

    moving = input("Enter a number 1 - 9: ")

    while moving.isdigit() == False or int(moving) > 9 or int(moving) < 1 or int(moving) in player1_dict[
        'moves'] or int(moving) in player2_dict['moves']:
        if moving.isdigit() != True:
            print("That won't work, lets try again! Please use a digit this time!")
        elif int(moving) in player2_dict["moves"] or int(moving) in player1_dict['moves']:
            print("Uh-oh, this board space is not empty!")
        elif int(moving) > 9:
            print("That's too big of a number! Lets try a single digit!")
        moving = input("Enter a number 1 - 9: ")

    moving = int(moving)

    if moving == 1:
        the_row[4][2][0] = ' ' + currently_moving_symbol + ' '
    elif moving == 2:
        the_row[4][2][2] = ' ' + currently_moving_symbol + ' '
    elif moving == 3:
        the_row[4][2][4] = ' ' + currently_moving_symbol + ' '
    elif moving == 4:
        the_row[2][2][0] = ' ' + currently_moving_symbol + ' '
    elif moving == 5:
        the_row[2][2][2] = ' ' + currently_moving_symbol + ' '
    elif moving == 6:
        the_row[2][2][4] = ' ' + currently_moving_symbol + ' '
    elif moving == 7:
        the_row[0][2][0] = ' ' + currently_moving_symbol + ' '
    elif moving == 8:
        the_row[0][2][2] = ' ' + currently_moving_symbol + ' '
    elif moving == 9:
        the_row[0][2][4] = ' ' + currently_moving_symbol + ' '

    if player1_dict['symbol'] == currently_moving_symbol:
        player1_dict['moves'].append(moving)
    elif player2_dict['symbol'] == currently_moving_symbol:
        player2_dict['moves'].append(moving)

    switch()


def check_for_winner():
    global winner
    combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1]]
    for combination in combinations:
        if combination[0] in player1_dict['moves'] and combination[1] in player1_dict['moves'] and combination[2] in player1_dict['moves']:
            winner = player1
            player1_dict['victories'] += 1
        elif combination[0] in player2_dict['moves'] and combination[1] in player2_dict['moves'] and combination[2] in player2_dict['moves']:
            winner = player2
            player2_dict['victories'] += 1
        elif len(player1_dict['moves']) + len(player2_dict['moves']) == 9:
            winner = 'Friendship'
            player1_dict['victories'] += 1
            player2_dict['victories'] += 1


def announce_move():
    if player1_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player1}!")
    elif player1_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player2}!")
    elif player2_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player2}!")
    elif player2_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player1}!")


print()
print()
print('Welcome to TicTacToe by Timur! To make a move use keypad on the right of your keyboard for reference.')

while game_on is True:
    if introduce_players:
        user_initial_input()
        user_history()
        introduce_players = False
    while n < 10:
        if n == 0:
            display(the_row)
        announce_move()
        move(currently_moving_symbol)
        display(the_row)
        if n > 3:
            check_for_winner()
            if winner != False:
                if winner == 'Friendship':
                    print(f"It's a draw! both {player1} and {player2} get a point!")
                elif winner == player1 or winner == player2:
                    print(f"Hurray! {winner} won and gets a victory point!")
                break
        n += 1

    print(f"The current score is {player1} : {player1_dict['victories']}, {player2} : {player2_dict['victories']}")

    while q2_bool == False:
        q2 = input('Would you like to play again? Y or N: ')
        if q2.lower() == 'y' or q2.lower() == 'n':
            q2_bool = True

    if q2 == "n":
        game_on = False
        break
    elif q2 == 'y':
        player1_dict['moves'] = []
        player2_dict['moves'] = []
        q2 = ""
        q2_bool = False
        n = 0
        the_row = [
            [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n',
             ['___', "|", '___', '|', '___']],
            '\n',
            [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n',
             ['___', "|", '___', '|', '___']],
            '\n',
            [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n',
             ['   ', "|", '   ', '|', '   ']]]
        currently_moving_X = True
        currently_moving_symbol = "X"
        winner = False

    announce_move()
    move(currently_moving_symbol)
    display(the_row)
