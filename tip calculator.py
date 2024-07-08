print("Welcome  to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_in_percentage = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
total_tip = total_bill * (tip_in_percentage / 100)
total = total_bill + total_tip
split = total / people 
print(f"Each person should pay: ${split:.2f}")


