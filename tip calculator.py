print("Welcome to the tip calculator!")

bill = input("\nWhat was the total bill? $ ")
tip = input("\nWhat percentage tip would you like to give? ")
customers = input("\nHow many people to split the bill? ")

share = ((float(tip) / 100) * round(float(bill), 2) + round(float(bill), 2)) / int(customers)

print(f"Each person should pay: ${round(share, 2)}")
