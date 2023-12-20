from utils.all import *
from typing import Any


def list2grid(l: list) -> dict:
    return {(x, y): l[x][y] for x in range(len(l)) for y in range(len(l[0]))}


def neighbor_tot(coords: tuple, total: int, G: dict) -> Any:
    x, y = coords
    for i in range(1, 3):
        yield (
            (x + i, y),
            total + sum(G.get((coords[0] + j, coords[1]), 0) for j in range(i)),
        )
        yield (
            (x, y + i),
            total + sum(G.get((coords[0], coords[1] + j), 0) for j in range(i)),
        )
        yield (
            (x, y - i),
            total + sum(G.get((coords[0], coords[1] - j), 0) for j in range(i)),
        )


input_17 = read_input_line(17, sep="\n")
input_17 = read_input_line("test_17", sep="\n")
input_17 = mapl(lambda x: list(int(y) for y in x), input_17)
start = (0, 0)
end = (len(input_17) - 1, len(input_17[0]) - 1)

G = list2grid(input_17)
visit: deque = deque([(start, 0, set())])
heat_loss: list = [INFINITY]

while visit:
    cur, loss, seen = visit.pop()  # type: ignore
    if not G.get(cur) or cur in seen:
        continue
    if loss > min(heat_loss):
        continue
    seen.add(cur)
    if cur == end:
        heat_loss.append(loss)
        print(loss)
        continue
    for i in neighbor_tot(cur, loss, G):
        visit.append((*i, seen))

print("Part One:", heat_loss)
