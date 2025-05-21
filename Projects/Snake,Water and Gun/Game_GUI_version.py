import tkinter as tk
import random

# Game logic
def play_round(user_choice):
    global user_score, computer_score, round_number

    if round_number > total_rounds:
        return

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        result = "You win this round!"
        user_score += 1
    else:
        result = "Computer wins this round!"
        computer_score += 1

    round_number += 1

    result_label.config(
        text=f"Round {round_number - 1}: {result}\nYou chose {user_choice}, Computer chose {computer_choice}"
    )
    score_label.config(
        text=f"Your Score: {user_score} | Computer Score: {computer_score}"
    )

    if round_number > total_rounds:
        if user_score > computer_score:
            final = "🎉 You won the game!"
        elif computer_score > user_score:
            final = "💻 Computer won the game!"
        else:
            final = "🤝 It's a tie!"

        result_label.config(text=f"Game Over!\n{final}")
        for btn in choice_buttons:
            btn.config(state="disabled")
        play_again_button.pack(pady=10)

def reset_game():
    global user_score, computer_score, round_number
    user_score = 0
    computer_score = 0
    round_number = 1
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    result_label.config(text="Choose: Snake, Water, or Gun")
    for btn in choice_buttons:
        btn.config(state="normal")
    play_again_button.pack_forget()

# Initialize game variables
choices = ["snake", "water", "gun"]
total_rounds = 3
user_score = 0
computer_score = 0
round_number = 1

# GUI Setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x350")
root.resizable(False, False)

title_label = tk.Label(root, text="🐍 Snake Water Gun Game 🔫", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12))
score_label.pack()

result_label = tk.Label(root, text="Choose: Snake, Water, or Gun", font=("Arial", 12))
result_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

choice_buttons = []
for choice in choices:
    btn = tk.Button(button_frame, text=choice.capitalize(), width=10, height=2, font=("Arial", 11),
                    command=lambda ch=choice: play_round(ch))
    btn.pack(side="left", padx=10)
    choice_buttons.append(btn)

play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12),
                              command=reset_game)

root.mainloop()
