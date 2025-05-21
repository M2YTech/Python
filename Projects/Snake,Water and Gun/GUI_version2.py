import tkinter as tk
from tkinter import messagebox
import random

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake, Water, Gun Game")
        self.root.geometry("400x500")
        self.root.config(bg="#f0f0f0")

        self.choices = ["snake", "water", "gun"]
        self.user_score = 0
        self.computer_score = 0
        self.round = 0
        self.total_rounds = 3

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="🐍 Snake, Water, Gun 🔫", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        self.title.pack(pady=20)

        self.round_label = tk.Label(self.root, text=f"Round {self.round + 1} of {self.total_rounds}", font=("Helvetica", 14), bg="#f0f0f0")
        self.round_label.pack()

        self.choice_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.choice_frame.pack(pady=20)

        for choice in self.choices:
            btn = tk.Button(self.choice_frame, text=choice.capitalize(), width=10, height=2, font=("Arial", 12, "bold"),
                            bg="#4CAF50", fg="white", command=lambda c=choice: self.play_round(c))
            btn.pack(pady=5)

        self.result_text = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#f0f0f0", fg="#000")
        self.result_text.pack(pady=20)

        self.score_text = tk.Label(self.root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12), bg="#f0f0f0", fg="#555")
        self.score_text.pack()

        self.restart_btn = tk.Button(self.root, text="Restart Game", font=("Arial", 10), command=self.reset_game, bg="#2196F3", fg="white")
        self.restart_btn.pack(pady=10)

    def play_round(self, user_choice):
        if self.round >= self.total_rounds:
            return

        computer_choice = random.choice(self.choices)
        result = ""

        if user_choice == computer_choice:
            result = "🤝 It's a draw!"
        elif (user_choice == "snake" and computer_choice == "water") or \
             (user_choice == "water" and computer_choice == "gun") or \
             (user_choice == "gun" and computer_choice == "snake"):
            self.user_score += 1
            result = "🎉 You win this round!"
        else:
            self.computer_score += 1
            result = "💻 Computer wins this round!"

        self.result_text.config(text=f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")
        self.round += 1
        self.score_text.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")
        self.round_label.config(text=f"Round {min(self.round + 1, self.total_rounds)} of {self.total_rounds}")

        if self.round == self.total_rounds:
            self.show_final_result()

    def show_final_result(self):
        if self.user_score > self.computer_score:
            final = "🏆 You won the game!"
        elif self.computer_score > self.user_score:
            final = "💻 Computer won the game!"
        else:
            final = "🤝 It's a tie game!"

        messagebox.showinfo("Game Over", final)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.round = 0
        self.result_text.config(text="")
        self.score_text.config(text="Score - You: 0 | Computer: 0")
        self.round_label.config(text=f"Round 1 of {self.total_rounds}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGame(root)
    root.mainloop()
