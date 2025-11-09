import tkinter as tk
import random

def play(choice):
    computer = random.choice(["rock", "paper", "scissors"])
    result = ""

    if choice == computer:
        result = "It's a tie!"
    elif (choice == "rock" and computer == "scissors") or \
         (choice == "paper" and computer == "rock") or \
         (choice == "scissors" and computer == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    label_result.config(text=f"Computer chose {computer}\n{result}")

# Window setup
root = tk.Tk()
root.title("Rock Paper Scissors")

label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_instructions.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

for option in ["rock", "paper", "scissors"]:
    tk.Button(frame_buttons, text=option.title(), width=10,
              command=lambda opt=option: play(opt)).pack(side="left", padx=5)

label_result = tk.Label(root, text="", font=("Arial", 12), pady=20)
label_result.pack()

root.mainloop()
