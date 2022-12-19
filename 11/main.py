from typing import Callable


FILENAME = "input.txt"


class Monkey:
    def __init__(
        self,
        monkey_id: int,
        items: list[int],
        worry_func: Callable[[int], int],
        divisible_test_int: int,
        test_true_id: int,
        test_false_id: int,
    ):
        self.monkey_id = monkey_id
        self.items = items
        self.worry_func = worry_func
        self.divisible_test_int = divisible_test_int
        self.test_true_id = test_true_id
        self.test_false_id = test_false_id
        self.inspected_num = 0

    def __repr__(self):
        return f"Monkey {self.monkey_id}: {', '.join(str(n) for n in self.items)}"


def get_input() -> list[Monkey]:
    monkey_list = list()

    with open(FILENAME) as file:
        monkeys = "".join(file.readlines())
        monkey_lines_list = monkeys.split("\n\n")

        for m in monkey_lines_list:
            m = m.split("\n")
            monkey_id = int(m[0][7:-1])
            items = list(map(int, m[1].split("items: ")[1].split(", ")))
            divisible_test_int = int(m[3].split("by ")[1])
            test_true_id = int(m[4].split("monkey ")[1])
            test_false_id = int(m[5].split("monkey ")[1])

            # Construct worry function
            func_str = m[2].split("= old ")[1].strip()
            opr, num_str = func_str[0], func_str[2:]

            if opr == "+":
                const = int(num_str)
                worry_func = (lambda const: lambda n: n + const)(const)

            elif opr == "*":
                if "old" in num_str:
                    worry_func = lambda n: n**2
                else:
                    const = int(num_str)
                    worry_func = (lambda const: lambda n: n * const)(const)

            else:
                raise ValueError(f"Unknown operation: {m[2]}")

            monkey_list.append(
                Monkey(
                    monkey_id,
                    items,
                    worry_func,
                    divisible_test_int,
                    test_true_id,
                    test_false_id,
                )
            )

    return monkey_list


def part_1():
    monkey_list = get_input()

    for __ in range(20):
        for m in monkey_list:
            while m.items:
                item = m.items.pop(0)
                m.inspected_num += 1
                item_worry_level = m.worry_func(item) // 3
                if item_worry_level % m.divisible_test_int == 0:
                    monkey_list[m.test_true_id].items.append(item_worry_level)
                else:
                    monkey_list[m.test_false_id].items.append(item_worry_level)

    L = list()

    for m in monkey_list:
        L.append(m.inspected_num)

    L.sort(reverse=True)

    result = L[0] * L[1]

    print(f"Answer is {result}")


def part_2():
    monkey_list = get_input()

    big_mod = 1
    for m in monkey_list:
        big_mod *= m.divisible_test_int

    for __ in range(10_000):
        for m in monkey_list:
            while m.items:
                item = m.items.pop(0)
                m.inspected_num += 1
                item_worry_level = m.worry_func(item) % big_mod
                if item_worry_level % m.divisible_test_int == 0:
                    monkey_list[m.test_true_id].items.append(item_worry_level)
                else:
                    monkey_list[m.test_false_id].items.append(item_worry_level)

    L = list()

    for m in monkey_list:
        L.append(m.inspected_num)

    L.sort(reverse=True)

    result = L[0] * L[1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
