cartons = [
    ["Not almond milk", "Wrong logo"],
    ["Not almond milk", "Wrong logo"],
    ["Almond milk", "Wrong logo"],
    ["Almond milk", "Right logo"],
    ["Almond milk", "Wrong logo"]
]

cart = []

wrongCartonsLookedAt = 0

for carton in cartons:
    typeOfMilk = carton[0]
    logo = carton[1]

    if typeOfMilk == "Almond milk" and logo == "Right logo":
        cart.append(carton)
        print("I got you almond milk")
        break
    else:
        wrongCartonsLookedAt += 1


if len(cart) == 0:
    cart.append("Beer")
    print("I got you beer")

#Using if elif and else
age = 16

print("Can you drink this beer?")
if age > 18:
    print("Yes!")
elif age > 16:
    print("Maybe, with a parent")
else:
    print("Sorry, wait until your 18th birthday!")
