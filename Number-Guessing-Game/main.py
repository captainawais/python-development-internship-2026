# =====================================================
# ADVANCED NUMBER GUESSING GAME
# =====================================================

import random


# =====================================================
# GAME INTRO
# =====================================================

def game_intro():

    print("\n" + "=" * 55)
    print("        ADVANCED NUMBER GUESSING GAME")
    print("=" * 55)

    print("\nSelect Difficulty Level:")
    print("1. Easy   (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard   (1 - 100)")


# =====================================================
# GET DIFFICULTY
# =====================================================

def get_difficulty():

    while True:

        choice = input("\nEnter difficulty level: ")

        if choice == "1":
            return 10, 5

        elif choice == "2":
            return 50, 7

        elif choice == "3":
            return 100, 10

        else:
            print("Invalid choice. Please try again.")


# =====================================================
# PLAY GAME
# =====================================================

def play_game():

    game_intro()

    max_number, attempts = get_difficulty()

    secret_number = random.randint(1, max_number)

    print(f"\nI have selected a number between 1 and {max_number}")
    print(f"You have {attempts} attempts to guess it.")

    score = 100

    while attempts > 0:

        try:

            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > max_number:
                print(f"Please enter number between 1 and {max_number}")
                continue

            # CORRECT GUESS
            if guess == secret_number:

                print("\n🎉 Congratulations!")
                print("You guessed the correct number!")

                print(f"🏆 Your Score: {score}")

                break

            # LOW GUESS
            elif guess < secret_number:
                print("📉 Too low!")

            # HIGH GUESS
            else:
                print("📈 Too high!")

            attempts -= 1
            score -= 10

            print(f"Remaining Attempts: {attempts}")

        except ValueError:
            print("Please enter a valid number.")

    else:

        print("\n❌ Game Over!")
        print(f"The correct number was: {secret_number}")


# =====================================================
# MAIN PROGRAM
# =====================================================

def main():

    while True:

        play_game()

        while True:

            replay = input(
                "\nDo you want to play again? (yes/no): "
            ).lower().strip()

            # PLAY AGAIN
            if replay in ["yes", "y"]:
                break

            # EXIT GAME
            elif replay in ["no", "n"]:

                print("\nThank you for playing!")
                return

            # INVALID INPUT
            else:
                print("Invalid input. Please type yes/y or no/n.")

                
# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":
    main()