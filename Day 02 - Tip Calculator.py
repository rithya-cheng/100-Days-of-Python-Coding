print("\n11. Day 02 - Project Tip Calculator")
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_per = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
each_person = round(float(total_bill) * (float(tip_per) / 100 + 1) / float(people), 2)
print(f"Each person should pay: {each_person}")