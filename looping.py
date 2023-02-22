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
import time

bacteria = "🌭"
generations = 10

for generation in range(0, generations):
    bacteria = bacteria * 2
    print(bacteria)
    time.sleep(0.5)
