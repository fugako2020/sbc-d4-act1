from random import randint


def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "fold" and computer_choice == "unfold":
        return "Player wins!"
    elif player_choice == "unfold" and computer_choice == "fold":
        return "Computer wins!"

player_choice = input("Enter 'fold' or 'unfold': ").strip().lower()
       # remove player not chooice
computer_choice = "fold" if randint(1, 2) == 1 else "unfold"

result = game_result(player_choice, computer_choice)
print(f"Player chose: {player_choice}")
print(f"Computer chose: {computer_choice}")
print(result)