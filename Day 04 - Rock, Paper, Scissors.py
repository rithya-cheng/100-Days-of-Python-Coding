print("\n9. Day 04 Project - Rock, Paper, Scissors")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
lists = ["rock", "paper", "scissor"]
user_choose = lists[user]
computer = random.randint(0, 2)
computer_choose = lists[computer]
print(f"You chose {user_choose}.")
print(f"Computer chose {computer_choose}.")
if (user == computer):
    print("Draw!")
elif (user - computer == 1 or user - computer == -2):
    print("You win!")
else:
    print("You lose!")