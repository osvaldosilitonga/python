import os
from player import Player

player = Player()

while True:
    os.system('cls')  # Clear Screen

    player.get_info()

    user_input = input("Please insert a one character (type \\exit to exit) : ").lower()
    if user_input == "\\exit":
        print("Well Played, Goodbye...")
        exit(0)

    if len(user_input) > 1 or len(user_input) == 0:
        continue

    player.check_character(user_input)

    if player.chance == 0:
        os.system('cls')  # Clear Screen
        player.get_info()
        print("\nYou Lose")
        break

    if player.is_win():
        os.system('cls')  # Clear Screen
        player.get_info()
        print("\nCongratulation, You win...")
        break
