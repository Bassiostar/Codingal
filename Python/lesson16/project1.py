import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.geometry("400x300")

        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        self.player_choice_label = tk.Label(master, text="Your choice: None", font=("Arial", 12))
        self.player_choice_label.pack(pady=5)

        self.computer_choice_label = tk.Label(master, text="Computer choice: None", font=("Arial", 12))
        self.computer_choice_label.pack(pady=5)

        self.result_label = tk.Label(master, text="Make your move!", font=("Arial", 16, "bold"), fg="blue")
        self.result_label.pack(pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, command=lambda: self.play_round("rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, command=lambda: self.play_round("paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, command=lambda: self.play_round("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.score_label = tk.Label(master, text="Score: You 0 - Computer 0 - Ties 0", font=("Arial", 10))
        self.score_label.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Score", command=self.reset_game)
        self.reset_button.pack(pady=5)

    def play_round(self, player_choice):
        computer_choice = get_computer_choice()

        self.player_choice_label.config(text=f"Your choice: {player_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice.capitalize()}")

        result = determine_winner(player_choice, computer_choice)
        self.result_label.config(text=result)

        if result == "You win!":
            self.player_score += 1
            self.result_label.config(fg="green")
        elif result == "Computer wins!":
            self.computer_score += 1
            self.result_label.config(fg="red")
        else:
            self.ties += 1
            self.result_label.config(fg="blue")

        self.update_score_display()

    def update_score_display(self):
        self.score_label.config(text=f"Score: You {self.player_score} - Computer {self.computer_score} - Ties {self.ties}")

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.update_score_display()
        self.player_choice_label.config(text="Your choice: None")
        self.computer_choice_label.config(text="Computer choice: None")
        self.result_label.config(text="Make your move!", fg="blue")
        messagebox.showinfo("Game Reset", "The game scores have been reset!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()