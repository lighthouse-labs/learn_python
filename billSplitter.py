# Your task is to build an app that takes a bill total, tip amount, and number of people as input
# and outputs how much each person should pay.
# The app will:

# 1. Ask for a total dollar amount
# 2. Ask for the percentage tip
# 3. Ask for the number of people splitting the bill
# 4. Use those numbers to calculate the amount that each person owes, printing it out to the terminal, along with the overall total

subtotal = float(input("Please add subtotal here => "))
numOfPeople = float(input("How many people ate => "))
tipAmount = float(input("How much do you want to tip eg 0.10 = 10% => "))
taxRate = 0.14
tax = subtotal * taxRate
total = subtotal + tax
tip = total * tipAmount
costPerPerson = (total + tip) / numOfPeople

print("The taxed owed is " + str(tax))
print("The total amount including tax is " + str(total))
print("each person owes" + str(costPerPerson))
