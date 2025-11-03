# Basic Rock–Paper–Scissors game (Updated 3rd November 2025)
# Author: danielawosoga


import random

def play_game():
    print("Welcome to Rock–Paper–Scissors!")
    
    # Valid choices
    choices = ["rock", "paper", "scissors"]

    while True:
        # Player input
        player = input("Enter rock, paper, or scissors: ").lower()
        
        # Input validation
        if player not in choices:
            print("Invalid input! Please type 'rock', 'paper', or 'scissors'.\n")
            continue

        # Computer choice
        computer = random.choice(choices)
        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        # Game logic
        if player == computer:
            print("It's a tie!\n")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!\n")
        else:
            print("You lose!\n")

        # Replay option
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye 👋")
            break

# Run the game
play_game()