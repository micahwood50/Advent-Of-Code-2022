FILENAME = "input.txt"


def get_input() -> list[list[str]]:
    heightmap = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            heightmap.append([ch for ch in line.strip()])

    return heightmap


def part_1():
    heightmap = get_input()
    min_dist_map = [[float("inf") for col in row] for row in heightmap]

    result = 0

    for row_i, row in enumerate(heightmap):
        for col_i, ch in enumerate(row):
            if ch == "S":
                start_coord = (col_i, row_i)
                heightmap[row_i][col_i] = "a"
            if ch == "E":
                end_coord = (col_i, row_i)
                heightmap[row_i][col_i] = "z"

    queue = [(start_coord, 0)]
    map_len = len(heightmap)
    map_width = len(heightmap[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (ci, ri), depth = queue.pop()

        if min_dist_map[ri][ci] <= depth:
            continue

        min_dist_map[ri][ci] = depth
        curr_height_ch = heightmap[ri][ci]

        for dx, dy in directions:
            cx, cy = ci + dx, ri + dy
            if 0 <= cx < map_width and 0 <= cy < map_len:
                if ord(heightmap[cy][cx]) - ord(curr_height_ch) <= 1:
                    queue.append(((cx, cy), depth + 1))

    ex, ey = end_coord

    print(f"Answer is {min_dist_map[ey][ex]}")


def part_2():
    heightmap = get_input()
    min_dist_map = [[float("-inf") for col in row] for row in heightmap]

    result = 0

    for row_i, row in enumerate(heightmap):
        for col_i, ch in enumerate(row):
            if ch == "S":
                start_coord = (col_i, row_i)
                heightmap[row_i][col_i] = "a"
            if ch == "E":
                end_coord = (col_i, row_i)
                heightmap[row_i][col_i] = "z"

    queue = [(end_coord, 0)]
    map_len = len(heightmap)
    map_width = len(heightmap[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (ci, ri), depth = queue.pop()

        if min_dist_map[ri][ci] >= depth:
            continue

        min_dist_map[ri][ci] = depth
        curr_height_ch = heightmap[ri][ci]

        for dx, dy in directions:
            cx, cy = ci + dx, ri + dy
            if 0 <= cx < map_width and 0 <= cy < map_len:
                if ord(heightmap[cy][cx]) - ord(curr_height_ch) >= -1:
                    queue.append(((cx, cy), depth - 1))

    result = float("inf")

    for row_i, row in enumerate(heightmap):
        for col_i, ch in enumerate(row):
            if ch == "a":
                result = min(result, -min_dist_map[row_i][col_i])

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
