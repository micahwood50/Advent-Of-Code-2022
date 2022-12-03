FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def split_rucksack(rucksack: str) -> tuple[str, str]:
    half_index = len(rucksack) // 2
    first_compartment = rucksack[:half_index]
    second_compartment = rucksack[half_index:]

    return first_compartment, second_compartment


def get_priority_score(ch: str) -> int:
    if ch.islower():
        return ord(ch) - ord("a") + 1
    return ord(ch) - ord("A") + 27


def part_1():
    result = 0
    rucksack_list = get_input()

    for rucksack in rucksack_list:
        c1, c2 = split_rucksack(rucksack)
        common_ch = list(set(c1) & set(c2))[0]
        result += get_priority_score(common_ch)

    print(f"Answer is {result}")


def part_2():
    result = 0
    rucksack_list = get_input()

    for r1, r2, r3 in zip(*[iter(rucksack_list)] * 3):
        common_ch = list(set(r1) & set(r2) & set(r3))[0]
        result += get_priority_score(common_ch)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
