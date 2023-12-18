from utils.all import *
import copy


class DIR(Enum):
    U = (-1, 0)
    D = (1, 0)
    L = (0, -1)
    R = (0, 1)


def inc(s: tuple, d: DIR):
    x, y = s
    nx, ny = d.value
    return x + nx, y + ny


def nxt(char: str, d: DIR) -> tuple:
    if char == ".":
        return (d,)
    elif char == "/":
        if d == DIR.R:
            return (DIR.U,)
        elif d == DIR.L:
            return (DIR.D,)
        if d == DIR.U:
            return (DIR.R,)
        elif d == DIR.D:
            return (DIR.L,)
    elif char == "\\":
        if d == DIR.R:
            return (DIR.D,)
        elif d == DIR.L:
            return (DIR.U,)
        if d == DIR.U:
            return (DIR.L,)
        elif d == DIR.D:
            return (DIR.R,)
    elif char == "-":
        if d in (DIR.L, DIR.R):
            return (d,)
        return (DIR.L, DIR.R)
    elif char == "|":
        if d in (DIR.U, DIR.D):
            return (d,)
        return (DIR.U, DIR.D)
    return ()


input_16 = read_input_line(16, sep="\n")
#  input_16 = read_input_line("test_16", sep="\n")
input_16 = mapl(list, input_16)
vis = copy.deepcopy(input_16)

G: dict = {
    (x, y): input_16[x][y]
    for x in range(len(input_16))
    for y in range(len(input_16[x]))
}


tot = 0
d = DIR.R
visit = deque([((0, 0), d)])
seen: defaultdict = defaultdict(int)
while visit:
    c, d = visit.popleft()
    while G.get(c) and (c, d) not in seen:
        seen[(c, d)] += 1
        char = G.get(c, "")
        vis[c[0]][c[1]] = "#"
        if char == "-" and d in (DIR.U, DIR.D):
            d = DIR.R
            visit.append((inc(c, DIR.L), DIR.L))
        if char == "|" and d in (DIR.L, DIR.R):
            d = DIR.D
            visit.append((inc(c, DIR.U), DIR.U))

        else:
            d = nxt(char, d)[0]
        dx, dy = d.value
        cx, cy = c
        c = (cx + dx, dy + cy)


print()
for o in input_16:
    for c in o:
        print(c, end="")
    print()

print()
for i in vis:
    for j in i:
        tot += j == "#"
        print(j, end="")
    print()

print(tot)
#  print(seen)
