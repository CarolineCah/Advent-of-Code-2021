numbers = map(int, open("numbers.txt", 'r').readlines())
print(len(numbers))

for x in numbers:
    for y in numbers:
        if x+y == 2020 and len(set([numbers.index(x), numbers.index(y)])) == 2:
            print('Part one: {}'.format(x*y))
           
        for z in numbers:
            if x+y+z == 2020 and len(set([numbers.index(x), numbers.index(y), numbers.index(z)])) == 3:
                print('Part two: {}'.format(x*y*z))

                print(reduce(lambda j,i: j*i, [j for j in numbers if (2020-j) in set(numbers)]))