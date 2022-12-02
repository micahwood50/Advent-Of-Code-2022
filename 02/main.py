FILENAME = "input.txt"


def get_input() -> list[list[str]]:
    strategy_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            strategy_list.append(line.strip().split())

    return strategy_list


def calculate_round_score(opp_move: str, your_move: str) -> int:
    o_int = ord(opp_move)
    u_int = ord(your_move) - ord("X") + ord("A")

    result = o_int - u_int

    if result == 1 or result == -2:
        return 0  # loss

    if result == -1 or result == 2:
        return 6  # win

    else:
        return 3


def calculate_move_score(opp_move: str, desired_result: str) -> int:
    if desired_result == "X":
        if opp_move == "A":
            return 3
        if opp_move == "B":
            return 1
        return 2
    if desired_result == "Y":
        if opp_move == "A":
            return 1
        if opp_move == "B":
            return 2
        return 3
    else:
        if opp_move == "A":
            return 2
        if opp_move == "B":
            return 3
        return 1


def part_1():
    strategy_list = get_input()
    result = 0

    for opp, you in strategy_list:
        round_result = calculate_round_score(opp, you)
        move_result = ord(you) - ord("X") + 1

        result += round_result + move_result

    print(f"Answer is {result}")


def part_2():
    strategy_list = get_input()
    result = 0

    for opp, desired_result in strategy_list:
        round_result = 3 * (ord(desired_result) - ord("X"))
        move_result = calculate_move_score(opp, desired_result)

        result += round_result + move_result

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
