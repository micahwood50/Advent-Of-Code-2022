FILENAME = "input.txt"


class SectionInterval:
    def __init__(self, first_section: int, last_section: int):
        self.first_section = first_section
        self.last_section = last_section

    def size(self) -> int:
        return self.last_section - self.first_section + 1

    def fully_contains(self, other) -> bool:
        return (
            self.first_section <= other.first_section
            and self.last_section >= other.last_section
        )

    def overlaps(self, other) -> bool:
        return (
            self.first_section <= other.first_section <= self.last_section
            or other.first_section <= self.first_section <= other.last_section
        )

    def __str__(self) -> str:
        return f"{self.first_section}-{self.last_section}"


def get_input() -> list[tuple[SectionInterval, SectionInterval]]:
    section_assignments = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            first_pair, second_pair = line.strip().split(",")
            first_assignment = SectionInterval(*map(int, first_pair.split("-")))
            second_assignment = SectionInterval(*map(int, second_pair.split("-")))

            section_assignments.append((first_assignment, second_assignment))

    return section_assignments


def part_1():
    section_assignments = get_input()
    result = 0

    for assignment_pair in section_assignments:
        a1, a2 = assignment_pair
        if a1.fully_contains(a2) or a2.fully_contains(a1):
            result += 1

    print(f"Answer is {result}")


def part_2():
    section_assignments = get_input()
    result = 0

    for assignment_pair in section_assignments:
        a1, a2 = assignment_pair
        if a1.overlaps(a2):
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
