def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    if mat:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                return "ValueError"

    if not mat[0]:
        return []

    rows = len(mat)
    cols = len(mat[0])

    result = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(mat[row][col])
        result.append(new_row)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if mat:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                return "ValueError"
    result = []
    for row in mat:
        result.append(sum(row))

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if mat:
        first_len = len(mat[0])
        for row in mat:
            if len(row) != first_len:
                return "ValueError"
    if not mat or not mat[0]:
        return []
    cols = len(mat[0])
    result = []

    for col in range(cols):
        col_sum = 0
        for row in mat:
            col_sum += row[col]
        result.append(col_sum)

    return result


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
print("\n\n########\n\n")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
print("\n\n########\n\n")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
