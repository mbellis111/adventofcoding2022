
def main():
    # https://adventofcode.com/2022/day/10
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    instructions = parse_file(lines)
    print(instructions)

    max_cycles = 220
    value, total = execute_cycles(instructions, max_cycles)
    print(value)
    print(total)

    print("Done!")


def execute_cycles(instructions, max_cycles):
    total = 0
    instruction_num = 0
    # cycles until instruction complete
    cycles_left = 0
    instruction = ('noop', 0)

    value = 1
    for i in range(0, max_cycles + 1):
        # check if we need to add
        if (i - 20) % 40 == 0:
            print("Cycle", i, "Value", value)
            total += i * value

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
    return value, total



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
