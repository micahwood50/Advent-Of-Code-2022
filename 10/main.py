FILENAME = "input.txt"


class Cpu:
    def __init__(self):
        self.x = 1

    def process(self, command_line: str):
        if command_line == "noop":
            return

        _, val = command_line.split()
        self.x += int(val)

    def get_X(self) -> int:
        return self.x


def get_input() -> list[str]:
    command_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            command_list.append(line.strip())

    return command_list


def part_1():
    command_list = get_input()
    result = 0

    my_cpu = Cpu()

    cycle_num = 1
    index = 0

    while index < len(command_list):
        if cycle_num % 40 == 20:
            result += cycle_num * my_cpu.get_X()

        command_line = command_list[index]

        if command_line.startswith("addx"):
            cycle_num += 1

            if cycle_num % 40 == 20:
                result += cycle_num * my_cpu.get_X()

            my_cpu.process(command_line)

        index += 1
        cycle_num += 1

    print(f"Answer is {result}")


def is_lit(x_value: int, cycle_num: int) -> bool:
    cycle_mod = (cycle_num - 1) % 40 + 1

    return x_value <= cycle_mod < x_value + 3


def print_CRT(lit_bool_list: list[bool]):
    for i, lb in enumerate(lit_bool_list):
        if i % 40 == 0:
            print()
        print("#" if lb else ".", end="")
    print()


def part_2():
    command_list = get_input()

    lit_bool_list = list()
    my_cpu = Cpu()

    cycle_num = 1
    index = 0

    while index < len(command_list):
        command_line = command_list[index]

        lit_bool_list.append(is_lit(my_cpu.get_X(), cycle_num))

        if command_line.startswith("addx"):
            cycle_num += 1
            lit_bool_list.append(is_lit(my_cpu.get_X(), cycle_num))

            my_cpu.process(command_line)

        index += 1
        cycle_num += 1

    print(f"Answer is...")
    print_CRT(lit_bool_list)


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
