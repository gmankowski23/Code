print("Welcome to Guess The Number!")
print(" ")
print("Would you like to view the rules?")
answer2 = input("Enter y/n : ")
if answer2 == "y":
    print(" ")
    print("RULES - ")
    print(" ")
    print("There are 3 different levels.")
    print("Level 1, 3 guesses, number 1 - 10")
    print("Level 2, 6 guesses, number 1 - 100")
    print("Level 3, 9 guesses,number 1 - 1000")
    print("If your guess is more than 100 away it will say WAY")
    print("If your guess is more than 200 away it will say WAY WAY")

print(" ")
print("Would you like to play?")
answer1 = input("Enter y/n : ")
if answer1 == "y":
    def game():

        def choose_level():
            print(" ")
            print("Choose a game level")
            print("1 = Easy")
            print("2 = Medium")
            print("3 = Hard")
            print(" ")
            gameLevel = int(input("Level Choice is : "))
            global gamelevelChoice
            gamelevelChoice = gameLevel

        choose_level()

        def level():

            global upperLimit
            global maxGuesses
  
            if gamelevelChoice == 1:
                upperLimit = 10
                maxGuesses = 3

            if gamelevelChoice == 2:
                upperLimit = 100
                maxGuesses = 6

            if gamelevelChoice == 3:
                upperLimit = 1000
                maxGuesses = 9

            else:
                print(" ")
                print("You need to choose an actual level")
                choose_level()

        level()

        def number():
            global computerNbr
            import random
            computerNbr = random.randint(1,upperLimit)
            print(" ")
            print("DEBUG - random number is : " + str(computerNbr))

        number()

        def guess():

            nbrofGuesses = 0

            while nbrofGuesses < maxGuesses:

                Guess = int(input("Enter a Number : "))

                if Guess > computerNbr + 200:
                    print("Your number is WAY WAY too high")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess > computerNbr + 100:
                    print("Your number is WAY too high")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess > computerNbr:
                    print("Your number is too high")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess < computerNbr - 200:
                    print("Your number is WAY WAY too low")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess < computerNbr - 100:
                    print("Your number is WAY too low")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess < computerNbr:
                    print("Your number is too low")
                    nbrofGuesses = nbrofGuesses + 1

                elif Guess == computerNbr:
                    print("Correct")
                    break

            while nbrofGuesses == maxGuesses:
                print(" ")
                print("Game Over...")
                print("Correct number was : " + str(computerNbr))
                break

        guess()

        def playAgain():

            print(" ")
            print("Would you like to play again?")
            answer = input("Enter y/n : ")
            if answer == "y":
                game()
            if answer == "n":
                print(" ")
                print("Thank You For Playing!")
                print(" ")

        playAgain()

    game()

elif answer1 == "n":
    print("-_-")
