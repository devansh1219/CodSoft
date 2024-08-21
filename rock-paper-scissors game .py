import random

def game():
    print("\nWelcome to Rock-Paper-Scissors!")
    print("Enter a choice (rock, paper, scissor) and I'll tell you who wins.")
    print("Type 'quit' at any time to exit the game.\n")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissor) or type 'quit' to exit: ").lower()

        if user_choice == "quit":
            print("Thanks for playing! See you next time.")
            break

        while user_choice not in ["rock", "paper", "scissor"]:
            user_choice = input("Invalid input. Please enter rock, paper or scissor: ").lower()

        possible_choices = ["rock", "paper", "scissor"]
        computer_choice = random.choice(possible_choices)

        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissor":
                print("Rock smashes scissor! You win!")
            else:
                print("Paper covers rock! I win.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissor cuts paper! I win.")
        elif user_choice == "scissor":
            if computer_choice == "paper":
                print("Scissor cuts paper! You win!")
            else:
                print("Rock smashes scissor! I win.")

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()
        if play_again != "yes":
            break

game()