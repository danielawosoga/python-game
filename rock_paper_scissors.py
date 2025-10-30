# rock_paper_scissors.py
# Basic Rock–Paper–Scissors game
# Author: danielawosoga
# Description: Player chooses rock, paper, or scissors. Computer randomly selects one and determines the winner.

import random

def main():
    print("Welcome to Rock–Paper–Scissors!")
    options = ["rock", "paper", "scissors"]

    # Ask for player input
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
