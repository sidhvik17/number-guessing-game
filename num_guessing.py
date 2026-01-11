import random
import time

def get_level():
    print("select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice=input("Enter your choice 1 (or) 2 (or) 3")
        if choice == "1":
            return 10
        elif choice == "2":
            return 5
        elif choice == "3":
            return 3
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
def play(high_score):
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    chances = get_level()
    print(f"\nGreat! You have {chances} chances. Let's begin!\n")
    k= random.randint(1,100)
    attempts=0
    start_time = time.time()

    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == k:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"\n Congratulations! You guessed the correct number in {attempts} attempts!")
            print(f" Time taken: {total_time} seconds")

            if high_score is None or attempts < high_score:
                print(" New High Score!")
                high_score = attempts

            return high_score

        elif guess < k:
            print("Incorrect! The number is greater.")
        else:
            print("Incorrect! The number is smaller.")

    print("\n You ran out of chances!")
    print(f"The correct number was {k}.\n")
    return high_score

def main():
    high_score = None

    while True:
        high_score = play(high_score)

        print("\nWould you like to play again?")
        again = input("Enter Y to play again or any other key to quit: ").lower()

        if again != 'y':
            print("\nThank you for playing! Goodbye ")
            break

        print(f"\n Current High Score: {high_score if high_score else 'No high score yet'}")
main()
