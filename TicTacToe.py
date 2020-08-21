the_row = [
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['___', "|", '___', '|', '___']],
    '\n',
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['___', "|", '___', '|', '___']],
    '\n',
    [['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   '], '\n', ['   ', "|", '   ', '|', '   ']]]

player1 = ""
player2 = ""
player1_dict = {'symbol': None, 'victories': '', 'moves': []}
player2_dict = {'symbol': None, 'victories': '', 'moves': []}
used_moves = []
currently_moving_X = True
currently_moving_symbol = 'X'
game_on = False
winner = 'absent'
introduce_players = True


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

    q1 = input(f"Would {player1} like to play as X? 'Y' or 'N'. 'N' will automatically assign {player2} as X.")
    q1 = q1.lower()
    if q1 != "y" and q1 != "n":
        while q1 != "y" and q1 != "n":
            q1 = input().lower()
            print(
                f"I am not sure I understand. Let's try again. Would {player1} like to play as 'x'? Please answer with 'Y' for 'yes' and 'N' for 'No'.")
        if q1 == 'y':
            player1_dict['symbol'] = "X"
            player2_dict['symbol'] = "O"
        elif q1 == 'n':
            player1_dict['symbol'] = "O"
            player2_dict['symbol'] = "X"


def move(currently_moving_symbol):
    # function that will alternate variables on the board after accepting user input and changes
    global the_row
    moving = input("Enter a number 1 - 9: ")

    while moving.isdigit() == False or int(moving) > 9 or int(moving) < 1 or moving in player1_dict[
        'moves'] or moving in player2_dict['moves'] or int(moving) in used_moves:
        if moving.isdigit() != True:
            print("That won't work, lets try again! Please use a digit this time!")
        elif int(moving) in used_moves:
            print("Uh-oh, this board space is not empty!")
        elif int(moving) > 9:
            print("That's too big of a number! Lets try a single digit!")
        moving = input("Enter a number 1 - 9: ")

    moving = int(moving)

    if moving == 1:
        the_row[4][2][0] = ' ' + currently_moving_symbol + ' '
        used_moves.append(1)
    elif moving == 2:
        the_row[4][2][2] = ' ' + currently_moving_symbol + ' '
        used_moves.append(2)
    elif moving == 3:
        the_row[4][2][4] = ' ' + currently_moving_symbol + ' '
        used_moves.append(3)
    elif moving == 4:
        the_row[2][2][0] = ' ' + currently_moving_symbol + ' '
        used_moves.append(4)
    elif moving == 5:
        the_row[2][2][2] = ' ' + currently_moving_symbol + ' '
        used_moves.append(5)
    elif moving == 6:
        the_row[2][2][4] = ' ' + currently_moving_symbol + ' '
        used_moves.append(6)
    elif moving == 7:
        the_row[0][2][0] = ' ' + currently_moving_symbol + ' '
        used_moves.append(7)
    elif moving == 8:
        the_row[0][2][2] = ' ' + currently_moving_symbol + ' '
        used_moves.append(8)
    elif moving == 9:
        the_row[0][2][4] = ' ' + currently_moving_symbol + ' '
        used_moves.append(9)
    switch()
#winning combinations are: (123),(456),(789),(951),(753),(741),(852),(963)

def announce_move():
    if player1_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player1}!")
    elif player1_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player2}!")
    elif player2_dict['symbol'] == "X" and currently_moving_X is True:
        print(f"Your move {player2}!")
    elif player2_dict['symbol'] == "X" and currently_moving_X is False:
        print(f"Your move {player1}!")


user_initial_input()
user_history()
display(the_row)

announce_move()
move(currently_moving_symbol)
display(the_row)

announce_move()
move(currently_moving_symbol)
display(the_row)

while game_on:
    if introduce_players == True:
        user_initial_input()
        user_history()
        introduce_players = False
    announce_move()
    move(currently_moving_symbol)
    display(the_row)