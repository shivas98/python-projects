def board_positions():
    '''
    This function shows the position of the game board in numbers
    
    '''
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')

def display_board(game_board):
    '''
    This function is used to display the game board with approriate markers placed in it
    '''
    print(' '+ game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3] + ' ')
    print('-----------')
    print(' '+ game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6] + ' ')
    print('-----------')
    print(' '+ game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9] + ' ')

def player_input():
    '''
    This function takes user input and allows user to choose whether he wants to play with X or O
    '''
    marker = ''

    while not marker in ['X', 'O']:
        marker = input('Player 1: Do you want to be X or O?\n').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def space_check(game_board, position):
    '''
    This function checks whether the space is empty on the position passed to place the marker
    '''
    return game_board[position] == ' '

def player_choice(game_board):
    '''
    This function takes user input for the position he/she wants to place marker on
    '''
    position = 0

    while not space_check(game_board, position):
        position = int(input('Please choose a position between (1-9) to place your marker. Reference of positions is provided above\n'))

    return position

def place_marker(game_board, position, marker):
    '''
    This function updates the board and place the player's marker on the board on the position he/she chooses
    '''
    game_board[position] = marker

def full_board_check(game_board):
    '''
    This function checks whether if any blank space is available on the board
    '''
    for i in range(1,10):
        if space_check(game_board, i):
            return True
    return False 

def win_check(game_board, player_marker):
    '''
    This function checks the win condition
    '''
    return (game_board[1] == game_board[2] == game_board[3] == player_marker) or \
    (game_board[4] == game_board[5] == game_board[6] == player_marker) or \
    (game_board[7] == game_board[8] == game_board[9] == player_marker) or \
    (game_board[1] == game_board[4] == game_board[7] == player_marker) or \
    (game_board[2] == game_board[5] == game_board[8] == player_marker) or \
    (game_board[3] == game_board[6] == game_board[9] == player_marker) or \
    (game_board[1] == game_board[5] == game_board[9] == player_marker) or \
    (game_board[3] == game_board[5] == game_board[7] == player_marker)

def game_replay():
    '''
    This function takes user input for replaying the game
    '''
    replay = ''

    while replay not in ['Y', 'N']:
        replay = input('Would you like to replay the game? Y or N\n').upper()

    return replay == 'Y'

if __name__ == '__main__':

    print('Welcome to Tic Tac Toe Game!!')
    
    while True:
        game_board = [' ']*10
        game_board[0] = '#'
        play_game = ''
        count = 0

        # Taking user input to start the game
        while play_game not in ['Y','N']:
            play_game = input('Are you ready to play the game? Y or N\n').upper()

            if play_game == 'Y':
                game_on = True
            elif play_game == 'N':
                game_on = False
            else:
                print('Please choose an appropriate option!\n')

        # showing playable position on the board
        print('These are the board positions that needs to be filled. Please remeber the positions')
        board_positions()

        player1_marker, player2_marker = player_input()
        while game_on:
            # deciding player's turn
            if count % 2 == 0:
                print(f'It\'s {player1_marker}\'s Turn\n')
                player_marker = player1_marker
                player_num = 1
            else:
                print(f'It\'s {player2_marker}\'s Turn\n')
                player_marker = player2_marker
                player_num = 2
            position = player_choice(game_board)
            place_marker(game_board, position, player_marker)
            display_board(game_board)

            if win_check(game_board,player_marker):
                print('\n'*5)
                display_board(game_board)
                print(f'Congratulations! Player {player_num}: You have won the game.')
                game_on = False
            elif not full_board_check(game_board):
                game_on = False
                print('\n\nIt\'s a draw')
            else:
                game_on = True

            count += 1

        if not game_replay():
            break
        print('\n'*100)