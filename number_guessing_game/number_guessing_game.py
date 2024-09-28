import random

def guess_the_number():
        
        user_input_number = int(input('Guess a number between 1 and 100.\n'))

        return user_input_number

def game_replay():
    replay = input('Do you like to play the game again?\n').upper()

    return replay == 'Y'

if __name__ == '__main__':
    print('Welcome to the Number Guessing Game!')

    game_on = input('Are you ready to play the game? Y or N\n').upper()

    print('You will get 5 chances to guess the number. Make your guess wisely!')

    while True:
        guesses = 1
        target_number = 5
        while guesses <= 5:
            print(f'Guess {guesses}')
            user_guess = guess_the_number()
            if user_guess == target_number:
                print(f'Congratulations!! You have guessed the number and it was {target_number}')
                break
            else:
                print('You have made the wrong guess. Please guess the number again.\n')

            guesses += 1

            if guesses == 5:
                print('You are out of guesses!\n')

        if not game_replay():
            break
        print('\n'*100)
