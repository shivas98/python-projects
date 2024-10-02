import random

def guess_the_word():
    guess_len = 0
    while guess_len != 1:
        user_guess = input('Guess a alphabet of the word. Please make a single alphabet guess.\n').lower()
        guess_len = len(user_guess)

    return user_guess

def is_replay():
    replay = input('Do you like to play the game again?\n').upper()

    return replay == 'Y'

if __name__ == '__main__':
    print('Welcome to Word Guessing game')
    words = ['rainbow', 'computer', 'juice', 'apple', 'python', 'maths', 'player', 'race','driver', 'water', 'board', 'football']
    play = input('Will you like to start the start? Y or N\n').upper()

    while True:
        target_word = random.choice(words)
        target_word_list = list(target_word)
        turns = 12

        display_text = list()
        for char in target_word_list:
            display_text.append('_')

        while turns > 0:
            print(' '.join(display_text))
            user_guess = guess_the_word()
            if user_guess in target_word_list:
                display_text[target_word_list.index(user_guess)] = user_guess
                target_word_list[target_word_list.index(user_guess)] = '_'
            else:
                print(f'You guessed wrong. \'{user_guess}\' is not in the word. Make other guess.')

            if ''.join(display_text) == target_word:
                print(f'Congratulations! you have guessed the word and Won the game.')
                print(f'The word was \'{target_word}\'')
                break

            turns -= 1

            if turns == 0:
                print('You are out of turns. You lost the game!')
                break
            print(f'You have {turns} turns left.')

        if not is_replay():
            break
        print('\n'*100)