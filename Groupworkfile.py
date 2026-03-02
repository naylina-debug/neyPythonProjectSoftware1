import random

def roll_dice():
    number = random.randint(1, 6)

    if number <= 2:
        return "Rock"
    elif number <= 4:
        return "Paper"
    else:
        return "Scissor"

print(" Welcome to 'Roll the Dice – Quest for Treasure Island' ")
print("Defeat the Island Guardian in 3 rounds to win the treasure!\n")

player_score = 0
guardian_score = 0

for round_number in range(1, 4):
    print(f"---  Challenge {round_number} ---")
    input("Press Enter to roll your magical dice... ")

    player_choice = roll_dice()
    guardian_choice = roll_dice()

    print("You rolled:", player_choice)
    print("Island Guardian rolled:", guardian_choice)

    if player_choice == guardian_choice:
        print(" It's a draw! The island trembles...")

    elif (player_choice == "Rock" and guardian_choice == "Scissor") or \
            (player_choice == "Scissor" and guardian_choice == "Paper") or \
            (player_choice == "Paper" and guardian_choice == "Rock"):
        print(" You win this challenge!")
        player_score += 1

    else:
        print(" Guardian wins this challenge!")
        guardian_score += 1

    print()

print(" Final Battle Result")
print("Your Score:", player_score)
print("Guardian Score:", guardian_score)

if player_score > guardian_score:
    print(" Congratulations! You found the hidden treasure!")
elif guardian_score > player_score:
    print(" The Guardian has defeated you. Try again!")
else:
    print(" The battle ends in a draw. The treasure remains hidden.")