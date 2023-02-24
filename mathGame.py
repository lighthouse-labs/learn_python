questions = [
    [1, 3],
    [15, 10],
    [215, 453]
]
score = 0

for a, b in questions:
    response = int(input("What is " + str(a) + " + " + str(b) + "?"))
    if response == a + b:
        print("Correct!")
        score += 1
    else:
        print("Wrong, try again!")

if score > len(questions) / 2:
    print("Welldone! Your score is " + str(score) +
          " out of " + str(len(questions)))
else:
    print("Roh roh! Your score is " + str(score) +
          " out of " + str(len(questions)) + ". Try again!")
