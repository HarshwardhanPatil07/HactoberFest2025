# Username:Madhuj275
#Aim : Implement Rock Paper Scissor Game using Algorithm
# Date: 28/10/24

import random
choices = ['rock', 'paper', 'scissors']
comp_choice = random.choice(choices)
player_wins = 0
comp_wins = 0
tie = 0

print("Welcome to [Rock Paper Scissors]")

while True:
    comp_choice = random.choice(choices)
    answer = input("----Type [play] to play, [exit] to exit------\n")
    
    if answer == "play":
        while True:
            choice = input("Enter you choice [rock/paper/scissors] :\n")
            choice = choice.lower()
            if choice == 'rock' and comp_choice == 'paper':
                print("- Computer chose paper\n[!] Computer Wins!")
                comp_wins += 1
                break
            elif choice == 'rock' and comp_choice == 'scissors':
                print("- Computer chose scissors\n[!] Yon Win!")
                player_wins += 1
                break
            elif choice == 'paper' and comp_choice == 'rock':
                print("- Computer chose rock\n[!] You Win!")
                player_wins += 1
                break
            elif choice == 'paper' and comp_choice == 'scissors':
                print("- Computer chose scissors\n[!] Computer Wins!")
                comp_wins += 1
                break
            elif choice == 'scissors' and comp_choice == 'rock':
                print("- Computer chose rock\n[!] Computer Wins!")
                comp_wins += 1
                break
            elif choice == 'scissors' and comp_choice == 'paper':
                print("- Computer chose paper\n[!] You Win!")
                player_wins += 1
                break
            elif choice == comp_choice:
                print(f"- Computer chose {comp_choice}\n[!] It's a Tie!")
                tie += 1
                break
            else: print(" Not a valid choice, Try again")
                
    elif answer == "exit":
        break
    else:
        print("[~] Not a valid answer, Try again")

print(f"- You won {player_wins} times\n- Computer wins {comp_wins} times\n- It was a tie {tie} times")
print("-------------- Thanks for playing!-------------------")
