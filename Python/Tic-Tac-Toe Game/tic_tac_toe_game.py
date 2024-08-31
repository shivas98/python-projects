def board_positions():
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')

def display_board(game_board):
    print(' '+ game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3] + ' ')
    print('-----------')
    print(' '+ game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6] + ' ')
    print('-----------')
    print(' '+ game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9] + ' ')

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?\n').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def space_check(game_board, position):
    return game_board[position] == ' '

def player_choice(game_board):
    position = 0

    while not space_check(game_board, position):
        position = int(input('Please choose a position between (1-9) to place your marker. Reference of positions is provided above\n'))

    return position

def place_marker(game_board, position, marker):
    game_board[position] = marker

def full_board_check(game_board):
    for i in range(1,11):
        if space_check(game_board, i):
            return False
    return True 

def win_check(game_board, player_marker):
    return (game_board[1] == game_board[2] == game_board[3] == player_marker)

if __name__ == '__main__':
    print('Welcome to Tic Tac Toe Game!!')
    game_board = [' ']*10
    game_board[0] = '#'
    play_game = ''
    count = 0
    # test = ['x','o','x','o','x','o','x','o','x','o']
    # print(game_board)
    while play_game not in ['Y','N']:
        play_game = input('Are you ready to play the game? Y or N\n').upper()

        if play_game == 'Y':
            game_on = True
        elif play_game == 'N':
            game_on = False
        else:
            print('Please choose an appropriate option!\n')

    print('These are the board positions that needs to be filled. Please remeber the positions')
    board_positions()

    player1_marker, player2_marker = player_input()
    
    
    while game_on:
        if count % 2 == 0:
            print(f'It is {player1_marker} Turn\n')
            player_marker = player1_marker
        else:
            print(f'It is {player2_marker} Turn\n')
            player_marker = player2_marker
        position = player_choice(game_board)
        place_marker(game_board, position, player_marker)
        display_board(game_board)
        print(game_board)
        if win_check(game_board,player_marker):
            display_board(game_board)
            print(f'Congratulations! Player {player_marker}: You have won the game.')
            game_on = False
        # else:
        #     full_board_check(game_board):
        #     game_on = True
            
        
        count += 1
