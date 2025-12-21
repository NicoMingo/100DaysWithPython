import random

def guesses(attempts):
    win_condition = False

    for i in range(attempts, 0, -1):
        true_or_false = True

        if win_condition == True:
            break
        elif i == 0:
            print("You lost!")
        else:
            print(f"You have {i} attempts to guess the number")

            while(true_or_false):
                try:
                    guess = int(input("Make a guess: "))

                    if type(guess) == int:
                        true_or_false = False
                except:
                    print("The guess should be a number!")
                    true_or_false = True

            if guess == secret_number:
                print("You won!!")
                win_condition = True
            elif guess > secret_number:
                print("Too high")
            elif guess < secret_number:
                print("Too low")


true_or_false = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

secret_number = int(random.uniform(1, 100))

# Comprobacion de comando
while(true_or_false):
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy" or difficulty == "hard":
        true_or_false = False
    else:
        print("The command entered is not valid")
        true_or_false = True


if difficulty == "easy":
    guesses(10)

elif difficulty == "hard":
    guesses(5)






######### Terminado el 21/12/2025 a las 20:00hs #########