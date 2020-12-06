import string

with open("input") as f:
    part1 = part2 = 0

    for group in f.read().split("\n\n"):
        answerspart1 = set()
        answerspart2 = set(string.ascii_lowercase)

        for person in group.split():
            answerspart1.update(person)
            answerspart2 &= set(person)

        part1 += len(answerspart1)
        part2 += len(answerspart2)

    print("Part 1:", part1)
    print("Part 2:", part2)
