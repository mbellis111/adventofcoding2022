
def main():
    # https://adventofcode.com/2022/day/10
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    instructions = parse_file(lines)
    # print(instructions)

    value = execute_instructions(instructions)
    print(value)

    print("Done!")


def execute_instructions(instructions):
    instruction_num = 0
    # cycles until instruction complete
    cycles_left = 0
    instruction = ('noop', 0)
    crt_board = []

    value = 1
    while instruction_num < len(instructions):

        # print the board when its complete
        if len(crt_board) == 40:
            print("".join(crt_board))
            crt_board = []

        if cycles_left == 0:
            # execute the last instruction, noops have a 0 to keep it easy
            value += instruction[1]
            instruction = instructions[instruction_num]
            instruction_num += 1
            op, amt = instruction
            if op == 'noop':
                cycles_left = 1
            elif op == 'addx':
                cycles_left = 2
        cycles_left -= 1

        # start printing the curr location of the sprint
        if value - 1 <= len(crt_board) <= value + 1:
            crt_board.append('#')
        else:
            crt_board.append('.')

    if crt_board:
        print("".join(crt_board))

    return value


def parse_file(lines):
    instructions = []
    for line in lines:
        vals = line.strip().split(" ")
        if len(vals) == 1:
            instructions.append((vals[0], 0))
        else:
            instructions.append((vals[0], int(vals[1])))
    return instructions


if __name__ == '__main__':
    main()
