FILENAME = "input.txt"


class Stacks:
    def __init__(self, input_str: str):
        lines = input_str.split("\n")
        length = (len(lines[0]) + 2) // 4
        self.stacks = [list() for __ in range(length)]

        for line in lines:
            if line[1] == "1":
                break

            for li in range(length):
                index = 4 * li + 1
                if line[index].isalpha():
                    self.stacks[li].insert(0, line[index])

    def move(self, num_moves: int, from_stack: int, to_stack: int):
        for __ in range(num_moves):
            if self.stacks[from_stack - 1]:
                self.stacks[to_stack - 1].append(self.stacks[from_stack - 1].pop())

    def move_9001(self, num_moves: int, from_stack: int, to_stack: int):
        self.stacks[to_stack - 1].extend(
            self.stacks[from_stack - 1][len(self.stacks[from_stack - 1]) - num_moves :]
        )
        self.stacks[from_stack - 1] = self.stacks[from_stack - 1][
            : len(self.stacks[from_stack - 1]) - num_moves
        ]

    def print_stacks(self):
        max_height = max(len(stack) for stack in self.stacks)

        for height_i in range(max_height - 1, -1, -1):
            for i in range(len(self.stacks)):
                print(
                    f"[{self.stacks[i][height_i]}]"
                    if len(self.stacks[i]) > height_i
                    else "   ",
                    end=" ",
                )
            print()

        for i in range(len(self.stacks)):
            print(f" {i+1} ", end=" ")
        print()

    def get_tops(self):
        result = ""

        for stack in self.stacks:
            if stack:
                result += stack[-1]

        return result


def get_input() -> tuple[Stacks, list[str]]:
    input_stacks = None
    move_list = list()

    stacks_str = ""

    with open(FILENAME) as file:
        move_flag = False

        for line in file.readlines():
            if not move_flag:
                if not line.strip():
                    input_stacks = Stacks(stacks_str)
                    move_flag = True

                stacks_str += line

            else:
                move_list.append(line.strip())

    return input_stacks, move_list


def part_1():
    stacks, moves = get_input()

    for move in moves:
        _, num_move = move.split("move ")
        num_move, from_to = num_move.split(" from ")
        from_int, to_int = map(int, from_to.split(" to "))
        num_move = int(num_move)

        stacks.move(num_move, from_int, to_int)

    print(f"Answer is {stacks.get_tops()}")


def part_2():
    stacks, moves = get_input()

    for move in moves:
        _, num_move = move.split("move ")
        num_move, from_to = num_move.split(" from ")
        from_int, to_int = map(int, from_to.split(" to "))
        num_move = int(num_move)

        stacks.move_9001(num_move, from_int, to_int)

    print(f"Answer is {stacks.get_tops()}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
