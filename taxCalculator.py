# The app will:

# Ask the user to input a subtotal.
# Calculate the tax owed using some(hard-coded) tax rate. This can be whatever you want, like 0.25.
# Print out a message with the amount of tax owed.
# Print out another message with the total owed including tax.

subtotal = float(input("Please add subtotal here => "))
taxRate = 0.14
tax = subtotal * taxRate
total = subtotal + tax

print('The taxed owed is ' + str(tax))
print("The total amount including tax is " + str(total))
