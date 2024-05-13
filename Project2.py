
import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == "rock" and you == "scissor":
        return False
    elif comp == "paper" and you == "rock":
        return False
    elif comp == "scissor" and you == "paper":
        return False
    elif comp == "rock" and you == "paper":
        return True
    elif comp == "paper" and you == "scissor":
        return True
    elif comp == "scissor" and you == "rock":
        return True

options = {"r": "rock", "p": "paper", "s": "scissor"}

random_number = random.choice(list(options.values()))
you_input = input("Player's turn: rock(r) paper(p) scissors(s)? ").lower()
you = options.get(you_input)

result = game(random_number, you)

print("Computer chose", random_number)
print("You chose", you)
if result is None:
    print("The game is a tie!")
elif result is False:
    print("You've lost the game! Better luck next time.")
elif result is True:
    print("Congratulations! You've won the game.")
