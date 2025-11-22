import random
while True:
    user_action = input("Enter a choice(Rock/Paper/Scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_actions = random.choice(possible_actions)
    print(f"\nYou chose{user_action} & Computer chose{computer_actions}.\n")

    if user_action == computer_actions:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_actions == "Scissors":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "Paper":
        if computer_actions == "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut Paper! You lose.")
    elif user_action == "Scissors":
        if computer_actions == "Paper":
            print("Scissors cut Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")
    play_again = input("Play again? (Y/N): ")
    if play_again != "Y":
        break