print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $\n"))

percentage=float(input("What percentage tip would you like to give? 10,12, or 15\n"))
final_bill= total_bill + (percentage/100 * total_bill)

total_people=float(input("How many people to split the bill?\n"))
per_pay= round(final_bill/total_people,2)

print(f"Each person should pay:${per_pay}")