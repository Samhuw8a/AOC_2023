from utils.all import *


D: dict = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def list2grid(l: list) -> dict:
    return {(x, y): l[x][y] for x in range(len(l)) for y in range(len(l[0]))}


input_18 = read_input_line(18, sep="\n")
#  input_18 = read_input_line("test_18", sep="\n")

input_18 = mapl(lambda x: (x.split(" ")[0], int(x.split(" ")[1])), input_18)

tot = 0
uheight = 0
dheight = 0
llenght = 0
rlenght = 0
x, y = 0, 0

for d, n in input_18:
    if d == "U":
        x -= n
        if x < 0:
            uheight = min(uheight, x)
    elif d == "D":
        x += n
        dheight = max(dheight, x)
    elif d == "R":
        y += n
        rlenght = max(rlenght, y)
    elif d == "L":
        y -= n
        if y < 0:
            llenght = min(llenght, y)

assert x == 0 and y == 0

height = uheight + dheight
lenght = llenght + rlenght
print(height, lenght)

matrix: defaultdict = defaultdict(lambda: ".")

for d, n in input_18:
    dx, dy = D[d]
    for _ in range(n):
        matrix[(x, y)] = "#"
        tot += 1
        x += dx
        y += dy


visit = deque([(1, 1)])
seen: set = set()
G = matrix

while visit:
    x, y = visit.popleft()
    #  if (x, y) in seen or G[(x, y)] == "#" or 0 <= x <= height or 0 <= y <= lenght:
    if (x, y) in seen or G[(x, y)] == "#":
        continue
    seen.add((x, y))
    tot += 1
    visit.extend(neighbors8_coords(x, y))


print("Part One:", tot)
