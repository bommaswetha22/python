import random

def generate():
    return random.randint(1,9)
def player_guess():
    return input('Digit a number between 1 and 9\n')
def game():
    right_guesses=0
    wrong_guesses=0
    while True:
        guess = player_guess()
        if guess == 'exit':
            break

        if int(guess) > generate():
           print('Higher value than the value generated!')
           wrong_guesses += 1
        elif int(guess) < generate():
            print('Lower value than the value generated!')
            wrong_guesses += 1
        else:
            print('You have guessed the correct value!!!!')
            right_guesses += 1

    print('You have entered', right_guesses,'correct guesses and', wrong_guesses,'wrong guesses')
    return right_guesses, wrong_guesses

game()

'''Digit a number between 1 and 9
2
Higher value than the value generated!
Digit a number between 1 and 9
4
You have guessed the correct value!!!!
Digit a number between 1 and 9'''
