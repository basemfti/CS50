import random

def main():
    while True:
        # Prompt the user for a positive integer level
        while True:
            level_input = input("Level: ")
            try:
                level = int(level_input)
                if level > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid positive integer.")

        # Randomly generate an integer between 1 and level, inclusive
        target_number = random.randint(1, level)
        print("Ready to accept guesses.")

        # Prompt the user to guess the integer
        while True:
            guess_input = input("Guess: ")
            try:
                guess = int(guess_input)
                if guess > 0:
                    break
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid positive integer.")

        # Check the guess and provide feedback
        if guess < 1 or guess > level:
            print("Too large!")
        elif guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()



