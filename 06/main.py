FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        for line in file.readlines():
            return line.strip()


def get_first_marker_index(datastream_str: str, marker_len: int) -> int:
    for i in range(len(datastream_str) - marker_len):
        marker = datastream_str[i : i + marker_len]
        if len(set(marker)) == marker_len:
            return i + marker_len


def part_1():
    datastream_str = get_input()

    print(f"Answer is {get_first_marker_index(datastream_str, 4)}")


def part_2():
    datastream_str = get_input()

    print(f"Answer is {get_first_marker_index(datastream_str, 14)}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
