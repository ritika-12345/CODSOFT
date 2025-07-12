import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ['Rock', 'Paper', 'Scissors']

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Display choices
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Your Score: {user_score}  |  Computer Score: {computer_score}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)
root.config(padx=20, pady=20)

# Labels
tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Arial', 14)).pack(pady=10)

user_choice_label = tk.Label(root, text="", font=('Arial', 12))
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="", font=('Arial', 12))
computer_choice_label.pack()

result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'), fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=('Arial', 12))
score_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Run the app
root.mainloop()