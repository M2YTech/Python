import tkinter as tk
from tkinter import messagebox
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Sound paths (replace with your own .wav or .mp3 files if desired)
SOUND_USER_WIN = "sounds\win.mp3"
SOUND_COMP_WIN = "sounds\lose.mp3"
SOUND_DRAW = "sounds\draw.mp3"

# Function to play sound
def play_sound(filename):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    except:
        pass  # Handle missing or incompatible sound silently

def get_winner(user, computer):
    if user == computer:
        return "draw"
    if (user == "snake" and computer == "water") or \
       (user == "water" and computer == "gun") or \
       (user == "gun" and computer == "snake"):
        return "user"
    return "computer"

class SnakeGunWaterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake, Water, Gun Game")
        self.root.geometry("400x500")
        self.root.config(bg="#1e1e2f")

        self.user_score = 0
        self.computer_score = 0
        self.round = 1
        self.total_rounds = 3

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="Snake 🐍  Water 💧  Gun 🔫", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="#ffdd57")
        self.title.pack(pady=20)

        self.round_label = tk.Label(self.root, text="Round 1 of 3", font=("Arial", 14), bg="#1e1e2f", fg="#a0a0ff")
        self.round_label.pack()

        self.choice_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.choice_frame.pack(pady=30)

        for choice in ["snake", "water", "gun"]:
            btn = tk.Button(self.choice_frame, text=choice.capitalize(), font=("Arial", 14), bg="#2e2e4d", fg="white",
                            width=10, command=lambda c=choice: self.play_round(c))
            btn.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#1e1e2f", fg="#ffffff")
        self.status_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="User: 0   Computer: 0", font=("Arial", 12), bg="#1e1e2f", fg="#ff9999")
        self.score_label.pack()

    def animate_status(self, text, color):
        self.status_label.config(text=text, fg=color)
        self.status_label.after(200, lambda: self.status_label.config(fg="#ffffff"))  # flash back to white

    def play_round(self, user_choice):
        if self.round > self.total_rounds:
            return

        computer_choice = random.choice(["snake", "water", "gun"])
        winner = get_winner(user_choice, computer_choice)

        if winner == "user":
            self.user_score += 1
            result = "You Win! 🎉"
            color = "#aaffaa"
        elif winner == "computer":
            self.computer_score += 1
            result = "Computer Wins! 💻"
            color = "#ff8888"
        else:
            result = "It's a Draw 🤝"
            color = "#ffffaa"

        status = f"You: {user_choice.capitalize()} | Computer: {computer_choice.capitalize()}\n{result}"
        self.animate_status(status, color)
        self.score_label.config(text=f"User: {self.user_score}   Computer: {self.computer_score}")
        self.round += 1
        self.round_label.config(text=f"Round {min(self.round, self.total_rounds)} of {self.total_rounds}")

        if self.round > self.total_rounds:
            self.root.after(500, self.show_final_result)

    def show_final_result(self):
        if self.user_score > self.computer_score:
            msg = "🎉 Congratulations! You won the game!"
            play_sound(SOUND_USER_WIN)
        elif self.computer_score > self.user_score:
            msg = "💻 Computer wins the game!"
            play_sound(SOUND_COMP_WIN)
        else:
            msg = "🤝 It's a tie!"
            play_sound(SOUND_DRAW)

        play_again = messagebox.askyesno("Game Over", f"{msg}\n\nDo you want to play again?")
        if play_again:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.round = 1
        self.status_label.config(text="")
        self.score_label.config(text="User: 0   Computer: 0")
        self.round_label.config(text="Round 1 of 3")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGunWaterApp(root)
    root.mainloop()
