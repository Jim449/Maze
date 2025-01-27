from random import randrange

for x in range(125):
    first = randrange(0, 2)
    second = randrange(0, 2)
    third = randrange(0, 2)
    fourth = randrange(0, 2)
    print(f"\"{first}{second}{third}{fourth}\"", end=", ")
