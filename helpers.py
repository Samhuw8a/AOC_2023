import re
from itertools import chain, product
from typing import (
    Callable,
    Union,
    Iterable,
    Any,
    TypeVar,
    Sequence,
    Optional,
    Generator,
    Dict,
)

T = TypeVar("T")


cat = "".join
inf = float("inf")
flatten = chain.from_iterable
DIGITS: tuple = tuple(str(i) for i in range(10))


def mapl(f: Callable, iterable) -> list:
    return list(map(f, iterable))


def mapt(f: Callable, iterable) -> tuple:
    return tuple(map(f, iterable))


def filterl(f: Callable, iterable) -> list:
    return list(filter(f, iterable))


def parse_multiline_string(s: str, datatype: type = str, sep: str = "\n") -> list:
    return mapl(datatype, s.split(sep))


def read_input(
    filename: Union[str, int], datatype: type = str, sep: str = "\n"
) -> list:
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"inputs/{filename}.txt") as f:
        return parse_multiline_string(f.read(), datatype, sep)


def read_input_line(filename: Union[str, int], sep: str = "") -> Sequence[str]:
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"inputs/{filename}.txt") as f:
        contents = f.read().strip()
        return contents if not sep else contents.split(sep)


def digits(line: str) -> list:
    return mapl(int, line)


def integers(text: str, negative: bool = True) -> tuple:
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))


def first_int(text: str) -> Optional[int]:
    if m := re.search(r"-?\d+", text):
        return int(m.group(0))  # type:ignore
    return None


def count_if(iterable: Iterable, pred: Callable[[Any], bool] = bool) -> int:
    return sum(1 for item in iterable if pred(item))


def first(iterable: Iterable, default: Any = None):
    return next(iter(iterable), default)


def filter_first(iterable: Iterable, pred: Callable[[Any], bool]):
    return first(el for el in iterable if pred(el))


def move_point(a: tuple, b: tuple) -> tuple:
    return tuple(p + q for p, q in zip(a, b))


def manhattan(a: tuple, b: tuple = (0, 0)) -> int:
    return sum(abs(p - q) for p, q in zip(a, b))


def sign(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def print_2d(lines: str) -> None:
    for line in lines:
        print(cat(line))


def maxval(d: dict) -> Any:
    return max(d.values())


def transpose(matrix: list) -> list:
    return list(zip(*matrix))


def bin2int(s: Any) -> int:
    return int(s, 2)


def neighbours(x: int, y: int, amount: int = 4) -> Generator:
    assert amount in {4, 5, 8, 9}
    for dy, dx in product((-1, 0, 1), repeat=2):
        if (
            (amount == 4 and abs(dx) != abs(dy))
            or (amount == 5 and abs(dx) + abs(dy) <= 1)
            or (amount == 8 and not dx == dy == 0)
            or amount == 9
        ):
            yield (x + dx, y + dy)


def complex_neighbours(pt: Any, amount: int = 4) -> Generator:
    assert amount in {4, 5, 8, 9}
    for dy, dx in product((-1, 0, 1), repeat=2):
        if (
            (amount == 4 and abs(dx) != abs(dy))
            or (amount == 5 and abs(dx) + abs(dy) <= 1)
            or (amount == 8 and not dx == dy == 0)
            or amount == 9
        ):
            yield pt + dx + dy * 1j


def neighbours_3d(x: int, y: int, z: int) -> Generator:
    yield from [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def list2grid(lines: list, pred: Callable[[Any], bool] = None) -> dict:
    return {
        (x, y): val
        for y, line in enumerate(lines)
        for x, val in enumerate(line)
        if (pred(val) if pred else True)  # type:ignore
    }


def grid2list(grid: Dict[tuple, Any], pred: Callable[[Any], bool] = bool) -> list:
    min_x, min_y = map(min, zip(*grid))
    if min_x < 0 or min_y < 0:  # type: ignore
        raise ValueError
    max_x, max_y = map(max, zip(*grid))
    lines = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]  # type:ignore
    for x, y in grid:
        if pred(grid[(x, y)]):
            lines[y][x] = "█"
    return lines
