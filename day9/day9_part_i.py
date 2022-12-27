
def main():
    # https://adventofcode.com/2022/day/4
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    instructions = parse_file(lines)
    print(instructions)

    prev = count_tail_positions(instructions)
    # print(prev)
    print(len(prev))

    print("Done!")


def move_rope(head, tail, amt, prev, xd, yd):
    for i in range(amt):
        head = (head[0] + xd, head[1] + yd)
        tail = move_tail(head, tail)
        # print("H", head, "T", tail)
        prev.add(tail)
    return head, tail


def count_tail_positions(instructions):
    # start at 0, 0
    prev = set()

    # start locations, on top of each other
    head = (0, 0)
    tail = (0, 0)
    prev.add(tail)

    for instruction in instructions:
        direction, amt = instruction
        if direction == 'R':
            head, tail = move_rope(head, tail, amt, prev, 1, 0)
        elif direction == 'L':
            head, tail = move_rope(head, tail, amt, prev, -1, 0)
        elif direction == 'U':
            head, tail = move_rope(head, tail, amt, prev, 0, 1)
        elif direction == 'D':
            head, tail = move_rope(head, tail, amt, prev, 0, -1)
    return prev


def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail

    xd = hx - tx
    yd = hy - ty

    if abs(xd) > 1 or abs(yd) > 1:
        return tx + restrict_diff(xd), ty + restrict_diff(yd)
    return tail


def restrict_diff(diff):
    if diff == 0:
        return diff
    elif diff > 0:
        return 1
    else:
        return -1


def parse_file(lines):
    instructions = []
    for line in lines:
        line = line.strip()
        left, right = line.split(" ")
        instructions.append((left, int(right)))
    return instructions


if __name__ == '__main__':
    main()
