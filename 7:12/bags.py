with open('input.txt') as file:
    input = file.readlines()
    input = [line.strip() for line in input]

# returns the first index of the color in the list


def get_num_bags(color):
    lines = [
        line for line in input if color in line and line.index(color) != 0]

    allColors = []

    if len(lines) == 0:
        return []

    else:
        colors = [line[:line.index(' bags ')] for line in lines]
        colors = [color for color in colors if color not in allColors]
# Recursive call, finds every bag with certain colors
        for color in colors:
            allColors.append(color)
            bags = get_num_bags(color)

            allColors += bags

        certainColors = []
        for color in allColors:
            if color not in certainColors:
                certainColors.append(color)

        return certainColors

        for color in colors:
            print(color)


colors = get_num_bags('shiny gold')
print(len(colors))

s = 'a bc'
print(s.index('bc'))
