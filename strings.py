# Okay, so for this exercise, your job is to use Python's string replace method to fix this string up and print the new version out to the console.

journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

print(journey
      .replace("tone", "town")
      .replace("whirl", "world")
      .replace("tray", "train")
      .replace("seedy", "city")
      .replace("Bored", "Born")
      .replace("or something", ""))
