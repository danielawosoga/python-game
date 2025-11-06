# Basic Rock–Paper–Scissors game (Updated 6th November 2025)
# Author: danielawosoga


import random

def play_game():
    print("Welcome to Rock–Paper–Scissors with Score Tracking!\n")

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        player = input("Enter rock, paper, or scissors: ").lower()
        if player not in choices:
            print("Invalid input! Please type 'rock', 'paper', or 'scissors'.\n")
            continue

        computer = random.choice(choices)
        print(f"You chose: {player}")
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!\n")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win this round!\n")
            player_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        # Display running score
        print(f"Current Score → You: {player_score} | Computer: {computer_score}\n")

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("\nFinal Score:")
            print(f"You: {player_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing! Goodbye 👋")
            break

play_game()
