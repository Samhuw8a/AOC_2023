from utils.all import *


class IndexType(Enum):
    COL = 0
    ROW = 1


input_13 = read_input_line(13, sep="\n\n")
input_13 = read_input_line("test_13", sep="\n\n")
input_13 = mapl(lambda x: mapl(list, x.split("\n")), input_13)


def is_mirrored(index: int, matrix: list) -> bool:
    if not matrix[index] == matrix[index + 1]:
        return False
    l = index
    r = index + 1
    while l >= 0 and r < len(matrix):
        if matrix[l] != matrix[r]:
            return False
        l -= 1
        r += 1

    return True


def parse_matrix(matrix: list) -> tuple:
    indexes: dict = {}
    found = 0
    tmatrix = transpose(matrix)
    for i in range(len(tmatrix) - 1):
        if is_mirrored(i, tmatrix):
            #  print(tmatrix[i], tmatrix[i + 1])
            #  print(f"found at COL: {i+1}")
            found = i + 1
            l = i
            r = i + 1
            while l >= 0 and r < len(tmatrix):
                indexes[l + 1] = r + 1
                l -= 1
                r += 1
            return IndexType.COL, indexes, found

    found = 0
    for i in range(len(matrix) - 1):
        if is_mirrored(i, matrix):
            #  print(matrix[i], matrix[i + 1])
            #  print(f"found at ROW: {i+1}")
            found = i + 1
            l = i
            r = i + 1
            while l >= 0 and r < len(tmatrix):
                indexes[l + 1] = r + 1
                l -= 1
                r += 1
            return IndexType.ROW, indexes, found

    return ()


answers = mapl(parse_matrix, input_13)
rows = 0
cols = 0
for t, indexes, found in answers:
    if t == IndexType.ROW:
        rows += found
    elif t == IndexType.COL:
        cols += found

print(rows, cols)
print("Part One:", (cols + 100 * rows))
