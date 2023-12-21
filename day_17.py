from utils.all import *
from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Any
import copy


def neighbor_tot(coords: tuple, d: str) -> Any:
    x, y = coords
    for i in range(1, 4):
        if d in "lr":
            yield ((x + i, y), "d")
        if d in "dr":
            yield ((x, y + i), "l")
        if d in "dl":
            yield ((x, y - i), "r")


def list2grid(l: list) -> dict:
    return {(x, y): l[x][y] for x in range(len(l)) for y in range(len(l[0]))}


input_17 = read_input_line(17, sep="\n")
input_17 = read_input_line("test_17", sep="\n")
input_17 = mapl(lambda x: list(int(y) for y in x), input_17)
vis = copy.deepcopy(input_17)
end = (len(input_17) - 1, len(input_17[0]) - 1)
G = list2grid(input_17)


def search(G: dict, src: Any, dst: Any) -> float:
    distance = defaultdict(lambda: INFINITY, {src: 0})
    queue = [(0, src, "ldr")]
    visited: set = set()

    while queue:
        dist, node, d = heapq.heappop(queue)

        if node == dst:
            return dist

        if node in visited:
            continue
        visited.add(node)
        val = G.get(node, ())

        if not val:
            continue

        for neighbor, direction in filter(
            lambda n: n[0] not in visited and G.get(n[0]), neighbor_tot(node, d)
        ):
            new_dist = dist + G.get(neighbor, 0.0)

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor, direction))

    return INFINITY


print(search(G, (0, 0), end))
