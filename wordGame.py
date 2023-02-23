# place = input("""
# Please name a place
# It can be a country
# Or a City
# Or even your favorite hangout. =>
# """)

# object = input("""
# Please name any object eg
# A hair brush,
# Guitar
# Or stress ball
# """)

# print("Just as I arrived at " + place +
#       ", I realized I had forgotten my " + object + ".")
# -----------------------------------------------------

proseString = """
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
"""
replacements = [
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

for prompt, placeholder in replacements:
    userInput = input(prompt)
    proseString = proseString.replace(placeholder, userInput)


print(proseString)
