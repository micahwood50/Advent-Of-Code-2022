FILENAME = "input.txt"


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Dir:
    def __init__(self, name: str):
        self.name = name
        self.items = list()

    def add_item(self, item):
        self.items.append(item)

    @property
    def size(self) -> int:
        result = 0

        for item in self.items:
            result += item.size

        return result

    def print_struct(self, num_indent: int = 0):
        tab = "  "
        print(f"{tab * num_indent}- {self.name} (dir)")

        num_indent += 1

        for item in self.items:
            if isinstance(item, File):
                print(f"{tab * num_indent}- {item.name} (file, size={item.size})")
            else:
                item.print_struct(num_indent)


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def construct_dir_struct(terminal_outputs: list[str]) -> Dir:
    line_index = 1

    home = Dir("/")
    dir_stack = [home]

    while line_index < len(terminal_outputs):
        curr_line = terminal_outputs[line_index]

        if curr_line[2:4] == "cd":
            dir_name = curr_line[5:]
            if dir_name == "..":
                if len(dir_stack) > 1:
                    dir_stack.pop()

            else:
                for item in dir_stack[-1].items:
                    if item.name == dir_name:
                        dir_stack.append(item)

            line_index += 1

        else:
            line_index += 1
            curr_line = terminal_outputs[line_index]

            while line_index < len(terminal_outputs) and curr_line[0] != "$":
                curr_line = terminal_outputs[line_index]

                if curr_line[0] == "d":
                    dir_name = curr_line[4:]
                    dir_stack[-1].add_item(Dir(dir_name))

                else:
                    file_size, file_name = curr_line.split()
                    file_size = int(file_size)

                    dir_stack[-1].add_item(File(file_name, file_size))

                line_index += 1
                if line_index < len(terminal_outputs):
                    curr_line = terminal_outputs[line_index]

    return home


def get_all_dirs(home: Dir) -> list[Dir]:
    result = [home]
    queue = [home]

    while queue:
        curr_dir = queue.pop()
        for item in curr_dir.items:
            if isinstance(item, Dir):
                result.append(item)
                queue.append(item)

    return result


def part_1():
    terminal_outputs = get_input()
    result = 0

    home = construct_dir_struct(terminal_outputs)

    dirs = get_all_dirs(home)

    for dir in dirs:
        if dir.size <= 100_000:
            result += dir.size

    print(f"Answer is {result}")


def part_2():
    terminal_outputs = get_input()

    total_disk_space = 70_000_000
    goal_unused_space = 30_000_000

    home = construct_dir_struct(terminal_outputs)

    dirs = get_all_dirs(home)
    dirs.sort(key=lambda d: d.size)

    curr_used_space = home.size
    curr_available_space = total_disk_space - curr_used_space

    for dir in dirs:
        dir_size = dir.size
        if curr_available_space + dir_size >= goal_unused_space:
            print(f"Answer is {dir_size}")
            break


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
