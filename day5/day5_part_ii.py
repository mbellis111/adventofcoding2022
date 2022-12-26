
def main():
    # https://adventofcode.com/2022/day/5
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    raw_stacks, instructions = parse_file(lines)
    # print(raw_stacks)
    print(instructions)

    stacks = create_stacks(raw_stacks)
    print(stacks)

    # make all the moves now
    for instruction in instructions:
        execute_instruction(stacks, instruction)

    # now lets see the top of each stack
    result = ''
    for stack in stacks:
        char = stack.pop()
        result += char
    print(result)

    print("Done!")


def execute_instruction(stacks, instruction):
    amount, start, end = instruction

    start_stack = stacks[start - 1]
    end_stack = stacks[end - 1]

    # move the crates but keep the order
    crates = []
    for i in range(amount):
        crate = start_stack.pop()
        crates.append(crate)

    # to keep the order just reverse the stack
    # could have use queue but this is easy
    crates = reversed(crates)
    for crate in crates:
        end_stack.append(crate)


def create_stacks(raw_stacks):
    stacks = []
    for raw_stack in raw_stacks:
        if raw_stack[0].isnumeric():
            stack = create_stack(raw_stack)
            stacks.append(stack)
    return stacks


def create_stack(raw_stack):
    # assumes proper formatting and starting with a number
    # ['1', 'W', 'R', 'F', ' ', ' ', ' ', ' ', ' ']
    stack = []
    for char in raw_stack[1:]:
        if char.isalpha():
            stack.append(char)
        else:
            return stack
    return stack


def parse_file(lines):
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3
    #
    # move 1 from 2 to 1
    # move 3 from 1 to 3

    stacks = []
    instructions = []
    parsing_stacks = True
    for line in lines:
        if not line.strip():
            parsing_stacks = False
            continue

        if parsing_stacks:
            stacks.append(list(line))
        else:
            # just add amount, from, and to
            vals = line.strip().split(" ")
            instructions.append((int(vals[1]), int(vals[3]), int(vals[5])))

    # rotate the stacks 90 degrees to work with it easier
    stacks = [list(reversed(col)) for col in zip(*stacks)]

    return stacks, instructions


if __name__ == '__main__':
    main()
