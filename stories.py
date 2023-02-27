# superBasic = [
#     'Title',
#     'Prose string with a REPLACEMENT, and also a SECOND_REPLACEMENT to illustrate the point',
#     [
#     ['Replacement prompt', 'REPLACMENT'],
#     ['Another replacement prompt', 'SECOND_REPLACMENT'],
#     ]

# ]

# stories = [
#     superBasic
# ]

letterHome = [
    # Title
    "A Letter Home",

    # Prose String
    """
    Hi mom,

    Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to
    COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY
    is the best place in the world to build a career around them. I'll need to start
    small-- At first, all I'll be allowed to do is to VERB near them, but when people 
    see how ADJECTIVE I can be, I'm sure to rise to the top.

    Don't worry about me, and tell sis to take care or my PERSONAL_ITEM. I'll be 
    sure to call every HOLIDAY.

    Love,

    NAME
    """,
    # Replacements
    [
        ["An occupation ", "OCCUPATION"],
        ["A country ", "COUNTRY"],
        ["A plural noun ", "PLURAL_NOUN"],
        ["A verb, like run, eat or dance ", "VERB"],
        ["An adjective like fun or warm ", "ADJECTIVE"],
        ["A title like manager, or chief ", "TITLE"],
        ["A personal item ", "PERSONAL_ITEM"],
        ["A holiday, like xmas or eater ", "HOLIDAY"],
        ["Your name ", "NAME"]
    ]
]

sale = [
    # Title
    "A Great Sale",

    # Prose String
    """
    SALE SALE SALE

    Today only: Buy NUMBER PLURAL_NOUN and get a free NOUN!

    Sign up for an exclusive METAL card and receive 50% off your first purchase!
    """,

    # Replacements
    [
        ["A number", "NUMBER"],
        ["A plural noun", "PLURAL_NOUN"],
        ["A noun", "NOUN"],
        ["A type of metal like aluminum or gold", "METAL"]
    ]
]

showAndTell = [
    # Title
    "Show and tell",
    "This is my pet ANIMAL. It's  the best-- No pet can VERB1 as ADVERB as it can. It's NUMBER years old, and it's name is NAME. You can VERB2 it if you want, but be careful, because it might VERB3.",

    # Replacements
    [
        ["An animal ", "ANIMAL"],
        ["A verb like 'run' or 'jump' ", "VERB1"],
        ["An adverb like 'quickly' or 'hard' ", "ADVERB"],
        ["A number ", "NUMBER"],
        ["A name", "NAME"],
        ["A transitive verb like 'touch' or 'notice' ", "VERB2"],
        ["A verb like 'run', 'jump' or 'bite' ", "VERB3"],
    ]
]

stories = [
    letterHome,
    sale,
    showAndTell
]

print("Select a story: ")
for index, story in enumerate(stories):
    title = story[0]
    print(str(index) + " - " + title)

selection = int(input("Choose a story by number -> "))
story = stories[selection]
proseString = story[1]
replacements = story[2]

for prompt, placeholder in replacements:
    userInput = input(prompt)
    proseString = proseString.replace(placeholder, userInput)
print(proseString)
