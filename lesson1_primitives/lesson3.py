import random

difficulty = 10
gameRunning = True
guesses = 0
number_to_guess = random.randint(1,difficulty)

print("I have chosen a number between 1 and " + str(difficulty) + ". Guess what it is! ")

while(gameRunning):
    guess = input("What is your guess? : ")

    if(len(guess) > 0):
        print("You guessed: " + guess)
        guesses = guesses + 1

        if(int(guess) > number_to_guess):
            print("Too High!")

        elif(int(guess) < number_to_guess):
            print("Too Low!")

        else:
            print("The number was: " + str(number_to_guess))
            print("You Win!!")
            print("It took you " + str(guesses) + " guesses!!")
            gameRunning = False
    else:
        print("You must enter a number!")
