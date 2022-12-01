FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    int_list_list = list()
    int_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            if line.strip():
                int_list.append(int(line))
            else:
                int_list_list.append(int_list)
                int_list = list()

    int_list_list.append(int_list)
    return int_list_list


def part_1():
    input = get_input()

    list_result = max(input, key=lambda l: sum(l))

    result = sum(list_result)

    print(f"Answer is {result}")


def part_2():
    input = get_input()

    list_result = sorted(input, key=lambda l: -sum(l))

    result = sum(sum(list_result[i]) for i in range(3))

    print(result)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
