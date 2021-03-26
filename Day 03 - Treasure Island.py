print("\n11. Day 03 Project - Treasure Island")
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
left_right = input("Do you want to go left or right? ").lower()
if (left_right == "left"):
    swim_wait = input("Do you want to swim or wait? ").lower()
    if (swim_wait == "wait"):
        door = input("Which door? red, blue or yellow? ").lower()
        if (door == "yellow"):
            print("You win!")
        else:
            print("Game Over!")
    else:
            print("Game Over!")
else:
    print("Game Over!")