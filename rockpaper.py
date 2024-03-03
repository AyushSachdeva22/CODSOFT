import random

def get_user_choice():
    while True:
        user_input = input("Choose rock , paper , or scissors : ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    if winner == "user":
        print(f"You win! {user} beats {computer}.")
    elif winner == "computer":
        print(f"You lose. {computer} beats {user}.")
    else:
        print("It's a tie!")

def main():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"Score: You {user_score}, Computer {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "y"]:
            continue
        elif play_again in ["no", "n"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    print(f"Game over. Final score: You {user_score}, Computer {computer_score}")

if __name__ == "__main__":
    main()