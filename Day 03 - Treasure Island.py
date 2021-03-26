print("\n11. Day 03 Project - Treasure Island")
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
left_right = input("Do you want to go left or right? ").lower()
if (left_right == "left"):
    swim_wait = input("You survived! Now, do you want to swim or wait? ").lower()
    if (swim_wait == "wait"):
        door = input("You survive the second stage! Now, which door? red, blue or yellow? ").lower()
        if (door == "yellow"):
            print("Congratulations! You win this game!")
        else:
            print("Sorry! Game Over!")
    else:
            print("Sorry! Game Over!")
else:
    print("Sorry! Game Over!")