foosballers = [
    "Mia",
    "Retta",
    "Augustine",
    "Jin",
    "Waylon",
    "Alphonso",
    "Sage",
    "Hubert",
    "Raymon",
    "Rebecca",
    "Monty",
    "Glen",
    "Christi",
    "Patrice",
    "Craig",
    "Dexter",
    "Wally",
    "Ian",
    "Pat"
]

# This var gets the length
listLength = len(foosballers)

# This var finds the median
median = listLength // 2

foosballers[median]
foosballers[median - 2: median + 3]
foosballers.insert(median, "AVG PLAYA")
# Add five more players with names of your choosing, to the bottom of the list-- They are unranked and we must therefore assume they are terrible.
foosballers += [
    "Wesley",
    "Lina",
    "Eleanor",
    "Kennedy",
    "Julie"
]
# Oh no-- Now "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this.
del foosballers[foosballers.index("AVG PLAYA")]
median = len(foosballers) // 2
foosballers.insert(median, "AVG PLAYA")

# Five more players show up, but they are ranked. Insert them at the appropriate location:

# - Lacy is one spot ahead of Hubert

# - Omar is one spot behind Rebecca

# - Otto is 8th best in the league

# - Chauncey is 10 spots from the bottom of the league
hubertIndex = foosballers.index("Hubert")
foosballers.insert(hubertIndex, "Lacy")
rebeccaIndex = foosballers.index("Rebecca")
foosballers.insert(rebeccaIndex, "Omar")
foosballers.insert(7, "Otto")
foosballers.insert(- 10, "Chandler")

print(median)
print("-------------------")
print(len(foosballers))
print("-------------------")
print(foosballers)
