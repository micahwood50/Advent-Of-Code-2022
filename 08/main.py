FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    matrix = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            matrix.append([int(d) for d in line.strip()])

    return matrix


def get_scenic_score(matrix: list[list[int]], row_i: int, col_i: int) -> int:
    result = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    this_tree_height = matrix[row_i][col_i]

    viewing_distances = list()

    for dx, dy in directions:
        viewing_score = 0
        curr_row, curr_col = row_i + dy, col_i + dx

        while 0 <= curr_row < len(matrix) and 0 <= curr_col < len(matrix[0]):
            viewing_score += 1

            if matrix[curr_row][curr_col] >= this_tree_height:
                break

            curr_row += dy
            curr_col += dx

        viewing_distances.append(viewing_score)

    for viewing_score in viewing_distances:
        result *= viewing_score

    return result


def part_1():
    matrix = get_input()
    visible_matrix = [
        [False for __ in range(len(matrix[0]))] for __ in range(len(matrix))
    ]

    visible_matrix[0][0] = True
    visible_matrix[0][-1] = True
    visible_matrix[-1][0] = True
    visible_matrix[-1][-1] = True

    # Visible from top
    for i in range(1, len(matrix[0]) - 1):
        depth = 0
        visible_matrix[depth][i] = True
        curr_max_height = matrix[depth][i]

        while curr_max_height < 9 and depth < len(matrix):
            if matrix[depth][i] > curr_max_height:
                visible_matrix[depth][i] = True
                curr_max_height = matrix[depth][i]
            depth += 1

    # Visible from bottom
    for i in range(1, len(matrix[0]) - 1):
        depth = len(matrix) - 1
        visible_matrix[depth][i] = True
        curr_max_height = matrix[depth][i]

        while curr_max_height < 9 and depth > 0:
            if matrix[depth][i] > curr_max_height:
                visible_matrix[depth][i] = True
                curr_max_height = matrix[depth][i]
            depth -= 1

    # Visible from left
    for i in range(1, len(matrix) - 1):
        depth = 0
        visible_matrix[i][depth] = True
        curr_max_height = matrix[i][depth]

        while curr_max_height < 9 and depth < len(matrix[0]):
            if matrix[i][depth] > curr_max_height:
                visible_matrix[i][depth] = True
                curr_max_height = matrix[i][depth]
            depth += 1

    # Visible from right
    for i in range(1, len(matrix) - 1):
        depth = len(matrix[0]) - 1
        visible_matrix[i][depth] = True
        curr_max_height = matrix[i][depth]

        while curr_max_height < 9 and depth > 0:
            if matrix[i][depth] > curr_max_height:
                visible_matrix[i][depth] = True
                curr_max_height = matrix[i][depth]
            depth -= 1

    result = 0

    for row in visible_matrix:
        result += row.count(True)

    print(f"Answer is {result}")


def part_2():
    matrix = get_input()
    result = 0

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            result = max(result, get_scenic_score(matrix, i, j))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
