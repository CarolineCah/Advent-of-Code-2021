part1 = 0
part2 = 0
for line in open("passwords.txt").readlines():
    arr = line.split()
    lower, upper = (int(i) for i in arr[0].split("-"))
    pw = arr[-1]
    req = arr[1][0]
    i, j = pw[lower - 1], pw[upper - 1]
    occurrences = pw.count(req)
    if lower <= occurrences <= upper:
        part1 += 1
    if (i == req) ^ (j == req):
        part2 += 1

print('Part one:', part1)
print('Part two:', part2)
