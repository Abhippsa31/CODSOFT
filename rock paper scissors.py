import random
print("Welcome to Rock, Paper, Scissors Game!")
print("======================================\n")
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    if user == "q":
        break

    if user not in options:
        print("Invalid choice.Please try again.")
        continue
    computer=random.choice(options)
    print(f"Computer choice:{computer}.")
    
    if user==computer:
        print("its a tie!")
    elif user == "rock" and computer == "scissors":
        print("You won!")
        user_wins += 1
    elif user == "paper" and computer == "rock":
        print("You won!")
        user_wins += 1
    elif user == "scissors" and computer == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1
        
    play_again=input("Do you want to play another round?(yes/no):").lower()
    if play_again!="yes":
        break  
      
print(f"Score: You{user_wins}-{computer_wins} Computer\n")

print("\n Final Score:")
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")

