import tkinter as tk
from random import choice
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

# Initialize scores
player_score = 0
computer_score = 0

# Use absolute paths to load sound files
select_sound = pygame.mixer.Sound(r"J:\Fidel_Python_basics\sounds\select.wav")
win_sound = pygame.mixer.Sound(r"J:\Fidel_Python_basics\sounds\win.wav")
lose_sound = pygame.mixer.Sound(r"J:\Fidel_Python_basics\sounds\lose.wav")
tie_sound = pygame.mixer.Sound(r"J:\Fidel_Python_basics\sounds\tie.wav")
reset_sound = pygame.mixer.Sound(r"J:\Fidel_Python_basics\sounds\reset.wav")

# Function to determine the winner
def determine_winner(player_choice):
    global player_score, computer_score
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)
    
    # Play select sound when a choice is made
    select_sound.play()

    # Display selections
    player_value_label.config(text=player_choice)
    computer_value_label.config(text=computer_choice)

    # Determine the result
    if player_choice == computer_choice:
        result_label.config(text="Tie!", fg="blue")
        tie_sound.play()  # Play tie sound
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result_label.config(text="Player Wins!", fg="green")
        player_score += 1
        win_sound.play()  # Play win sound
    else:
        result_label.config(text="Computer Wins!", fg="red")
        computer_score += 1
        lose_sound.play()  # Play lose sound

    # Update the scoreboard
    player_score_label.config(text=str(player_score))
    computer_score_label.config(text=str(computer_score))

# Play reset sound in reset_game function
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_value_label.config(text="----")
    computer_value_label.config(text="----")
    result_label.config(text="Result will be displayed here", fg="black")
    player_score_label.config(text="0")
    computer_score_label.config(text="0")
    
    # Play reset sound
    reset_sound.play()

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x400")
window.config(bg="lightblue")

# Title label
title_label = tk.Label(window, text="Rock-Paper-Scissor", font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Player selection buttons
selection_frame = tk.Frame(window, bg="lightblue")
selection_frame.pack(pady=10)

rock_button = tk.Button(selection_frame, text="Rock", font=("Arial", 14), command=lambda: determine_winner('Rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(selection_frame, text="Paper", font=("Arial", 14), command=lambda: determine_winner('Paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(selection_frame, text="Scissors", font=("Arial", 14), command=lambda: determine_winner('Scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Selected Values
values_frame = tk.Frame(window, bg="lightblue")
values_frame.pack(pady=10)

player_label = tk.Label(values_frame, text="Player Selected: ", font=("Arial", 12), bg="lightblue")
player_label.grid(row=0, column=0, padx=10)
player_value_label = tk.Label(values_frame, text="----", font=("Arial", 12), bg="lightblue")
player_value_label.grid(row=0, column=1, padx=10)

computer_label = tk.Label(values_frame, text="Computer Selected: ", font=("Arial", 12), bg="lightblue")
computer_label.grid(row=1, column=0, padx=10)
computer_value_label = tk.Label(values_frame, text="----", font=("Arial", 12), bg="lightblue")
computer_value_label.grid(row=1, column=1, padx=10)

# Scoreboard
scoreboard_frame = tk.Frame(window, bg="lightblue")
scoreboard_frame.pack(pady=10)

player_score_text = tk.Label(scoreboard_frame, text="P", font=("Arial", 12), bg="lightblue")
player_score_text.grid(row=0, column=0, padx=20)
computer_score_text = tk.Label(scoreboard_frame, text="C", font=("Arial", 12), bg="lightblue")
computer_score_text.grid(row=0, column=1, padx=20)

player_score_label = tk.Label(scoreboard_frame, text="0", font=("Arial", 12), bg="lightblue")
player_score_label.grid(row=1, column=0, padx=20)
computer_score_label = tk.Label(scoreboard_frame, text="0", font=("Arial", 12), bg="lightblue")
computer_score_label.grid(row=1, column=1, padx=20)

# Result
result_label = tk.Label(window, text="Result will be displayed here", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=10)

# Reset Button
reset_button = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter loop
window.mainloop()
