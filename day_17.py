from utils.all import *
from typing import Any


def list2grid(l: list) -> dict:
    return {(x, y): l[x][y] for x in range(len(l)) for y in range(len(l[0]))}


def neighbor_tot(coords: tuple, total: int) -> Any:
    x, y = coords
    for i in range(1, 4):
        yield ((x + i, y), total)
        yield ((x, y + i), total)
        yield ((x, y - i), total)


input_17 = read_input_line(17, sep="\n")
input_17 = read_input_line("test_17", sep="\n")
input_17 = mapl(lambda x: list(int(y) for y in x), input_17)
start = (0, 0)
end = (len(input_17) - 1, len(input_17[0]) - 1)

G = list2grid(input_17)
visit: list = [(start, 0)]
heat_loss: list = []
seen: set = set()

while visit:
    cur, loss = heapq.heappop(visit)  # type: ignore
    if not G.get(cur) or cur in seen:
        continue
    seen.add(cur)
    if cur == end:
        heat_loss.append(loss)
        print(loss)
        continue
    loss += G[cur]
    for i in neighbor_tot(cur, loss):
        heapq.heappush(visit, i)

print("Part One:", heat_loss)
