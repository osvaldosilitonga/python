import os
from player import Player

player = Player(5)

message = ""
while True:
    os.system('cls')  # Clear Screen

    player.get_info()
    print()  # Extra space
    print(message)
    message = ""

    user_input = input("Please insert a one character (type \\exit to exit) : ").lower()
    if user_input == "\\exit":
        print("Well Played, Goodbye...")
        exit(0)

    if len(user_input) > 1 or len(user_input) == 0:
        message = "Invalid Input...\n"
        continue

    player.check_character(user_input)

    if player.chance == 0:
        player.get_info()
        print("\nYou Lose")
        break

    if player.is_win():
        player.get_info()
        print("\nCongratulation, You win...")
        break
