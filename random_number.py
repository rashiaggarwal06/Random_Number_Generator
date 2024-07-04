import random

target = random.randint(1, 100)

userInput = input("Guess the target(P) or Quit(Q): ")
print(userInput)
while True:
    if userInput == "Q":
        break
    elif userInput == "P":
        userGuess = int(input("Guess the number (Between 1 and 100): "))
        if userGuess == target:
            print("Success! You have guessed the correct number")
            break
        elif userGuess < target:
            print("Your number is smaller than the target. Try again with a bigger guess!")
        elif userGuess > target:
            print("Your number is larger than the target. Try again with a smaller guess!")
        else:
            print("Invalid input. Please enter 'P' to play or 'Q' to quit.")
            userInput = input("Guess the target(P) or Quit(Q): ") 

print("------------GAME OVER---------------")