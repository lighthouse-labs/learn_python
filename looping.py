# clothing = [
#     "Shirt",
#     "Pants",
#     "Socks",
# ]

# for item in clothing:
#     foldedItem = "Folded " + item
#     print(foldedItem)

# print("This is not part of the `for` loop")
# ----------------------------------------------

# instructionSteps = [
#     "turn left",
#     "go straight",
#     "turn right",
#     "keep going until you see the dog statue",
#     "turn right",
#     "turn right again",
#     "park right on the sidewalk"
# ]

# instructions = "First, "

# instructionStepsButScreamed = []

# for nextInstruction in instructionSteps:
#     upperInstruction = nextInstruction.upper()
#     instructionStepsButScreamed.append(upperInstruction)

# print(instructionStepsButScreamed)
# --------------------------------------

# Time is a library in Python
# import time

# bacteria = "🌭"
# generations = 10

# for generation in range(0, generations):
#     bacteria = bacteria * 2
#     print(bacteria)
#     time.sleep(0.5)

# ----------------------------------------


# actors = [
#     "Nathan Fallion",
#     "Gina Torres",
#     "Alan Tudyk",
#     "Morena Baccarin",
#     "Adam Baldwin",
#     "Jewel Staite",
#     "Sean Maher",
#     "Summer Glau",
#     "Ron Glass"
# ]

# roles = [
#     "Captain Malcolm Reynalds",
#     "Zoe Washburn",
#     "Hoban Washburn",
#     "Inara Serra",
#     "Jayne Cobb",
#     "Kaylee Frye",
#     "Dr. Simon Tam",
#     "River Tam",
#     "Derrial Book",
# ]

actorRoles = [
    ["Nathan Fallion", "Captain Malcolm Reynalds"],
    ["Gina Torres", "Zoe Washburn"],
    ["Alan Tudyk", "Hoban Washburn"],
    ["Morena Baccarin", "Inara Serra"],
    ["Adam Baldwin", "Jayne Cobb"],
    ["Jewel Staite", "Kaylee Frye"],
    ["Sean Maher", "Dr. Simon Tam"],
    ["Summer Glau", "River Tam"],
    ["Ron Glass", "Derrial Book"],

]
print("Featuring:\n=-=-=-=-=-=-=-=")
for actorRole in actorRoles:
    actor = actorRole[0]
    role = actorRole[1]
    print(actor + " as " + role)
