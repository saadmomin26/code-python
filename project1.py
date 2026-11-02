# '''
# 1 for snack
# -1 for water
# 0 for gun
# '''
# import random
# computer=random.choice([0, 1, -1]) #it will chose randon num betn 0,1,-1
# youstr=input("Enter your choise:")
# youdict={"snack":1,"water":-1,"gun":0}
# reverseDict={1:"snack",-1:"water",0:"gun"}

# you=youdict[youstr]
# print(f"you chose:{reverseDict[you]}\n Coumpure chose:{reverseDict[computer]}")

# if computer == you:
#     print("match draw")
# else:
#     if (computer ==- 1 and you==1):
#         print("you win")
#     elif(computer ==- 1 and you==0):
#         print("you lose")
#     elif(computer == 1 and you==-1):
#         print("you lose")
#     elif(computer == 1 and you==0):
#         print("you won")
#     elif(computer == 0 and you==1):
#         print("you lose")
#     elif(computer == 0 and you==-1):
#         print("you won")
#     else:
#         print("something went wrong!")

import tkinter as tk
from tkinter import messagebox
import random

# Mapping for game logic
choice_map = {"Snack": 1, "Water": -1, "Gun": 0}
reverse_map = {1: "Snack", -1: "Water", 0: "Gun"}

# Core game logic
def play(user_choice_str):
    user_choice = choice_map[user_choice_str]
    computer_choice = random.choice([0, 1, -1])
    
    result_text = f"You chose: {user_choice_str}\nComputer chose: {reverse_map[computer_choice]}\n"

    if computer_choice == user_choice:
        result_text += "Result: Match Draw"
    else:
        if (computer_choice == -1 and user_choice == 1) or \
           (computer_choice == 1 and user_choice == 0) or \
           (computer_choice == 0 and user_choice == -1):
            result_text += "Result: You Win 🎉"
        else:
            result_text += "Result: You Lose 😞"
    
    result_label.config(text=result_text)

# GUI Setup
root = tk.Tk()
root.title("Snacks-Water-Gun Game")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

title = tk.Label(root, text="Snacks 🥨 Water 💧 Gun 🔫 Game", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

btn_snack = tk.Button(button_frame, text="Snack 🥨", width=12, bg="#ffc107", fg="black", font=("Arial", 12),
                      command=lambda: play("Snack"))
btn_snack.grid(row=0, column=0, padx=10)

btn_water = tk.Button(button_frame, text="Water 💧", width=12, bg="#17a2b8", fg="white", font=("Arial", 12),
                      command=lambda: play("Water"))
btn_water.grid(row=0, column=1, padx=10)

btn_gun = tk.Button(button_frame, text="Gun 🔫", width=12, bg="#dc3545", fg="white", font=("Arial", 12),
                    command=lambda: play("Gun"))
btn_gun.grid(row=0, column=2, padx=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 13), bg="#f0f8ff", fg="#000")
result_label.pack(pady=20)

# Run the app
root.mainloop()
