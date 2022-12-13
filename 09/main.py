FILENAME = "input.txt"


class KnotNode:
    def __init__(self, name: str = "?"):
        self.name = name
        self.coord = (0, 0)
        self.visited_set = {(0, 0)}
        self.next_knot = None

    def set_next(self, next_knot):
        self.next_knot = next_knot

    def _helper_move(self, direction: str):
        cx, cy = self.coord

        if "U" in direction:
            cy += 1

        if "D" in direction:
            cy -= 1

        if "L" in direction:
            cx -= 1

        if "R" in direction:
            cx += 1

        self.coord = (cx, cy)
        self.visited_set.add(self.coord)

        if self.next_knot is not None:
            nx, ny = self.next_knot.coord

            if abs(nx - cx) > 1 or abs(ny - cy) > 1:
                if nx != cx and ny != cy:
                    # next knot must move diagonally
                    if abs(nx + 1 - cx) <= 1 and abs(ny + 1 - cy) <= 1:
                        self.next_knot._helper_move("UR")

                    elif abs(nx + 1 - cx) <= 1 and abs(ny - 1 - cy) <= 1:
                        self.next_knot._helper_move("DR")

                    elif abs(nx - 1 - cx) <= 1 and abs(ny + 1 - cy) <= 1:
                        self.next_knot._helper_move("UL")

                    elif abs(nx - 1 - cx) <= 1 and abs(ny - 1 - cy) <= 1:
                        self.next_knot._helper_move("DL")

                else:
                    # Otherwise next knot just move horizontally or vertically
                    if abs(nx + 1 - cx) <= 1 and abs(ny - cy) <= 1:
                        self.next_knot._helper_move("R")

                    elif abs(nx - 1 - cx) <= 1 and abs(ny - cy) <= 1:
                        self.next_knot._helper_move("L")

                    elif abs(nx - cx) <= 1 and abs(ny + 1 - cy) <= 1:
                        self.next_knot._helper_move("U")

                    elif abs(nx - cx) <= 1 and abs(ny - 1 - cy) <= 1:
                        self.next_knot._helper_move("D")

    def move(self, direction: str, distance: int):
        for __ in range(distance):
            self._helper_move(direction)


def get_input() -> list[tuple[str, int]]:
    move_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            direction, distance = line.strip().split()
            distance = int(distance)
            move_list.append((direction, distance))

    return move_list


def part_1():
    move_list = get_input()

    head_knots = KnotNode("H")
    head_knots.set_next(KnotNode("T"))

    for dir, dist in move_list:
        head_knots.move(dir, dist)

    print(f"Answer is {len(head_knots.next_knot.visited_set)}")


def part_2():
    move_list = get_input()

    head_knots = KnotNode("H")
    knot_list = [head_knots]

    for kn in range(1, 10):
        this_knot = KnotNode(str(kn))
        knot_list[-1].set_next(this_knot)
        knot_list.append(this_knot)

    for dir, dist in move_list:
        head_knots.move(dir, dist)

    print(f"Answer is {len(knot_list[-1].visited_set)}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
