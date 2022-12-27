
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


def move_rope(rope, amt, prev, xd, yd, rope_len):
    for i in range(amt):
        head = rope[0]
        head = (head[0] + xd, head[1] + yd)
        rope[0] = head
        prior = head
        for n in range(1, rope_len):
            tail = rope[n]
            tail = move_tail(prior, tail)
            prior = tail
            rope[n] = prior
        # add the last tail
        prev.add(prior)
    return rope


def count_tail_positions(instructions):
    # start at 0, 0
    prev = set()

    # rope len is 10
    rope_len = 10

    # start locations, on top of each other
    rope = []
    for _ in range(rope_len):
        rope.append((0, 0))
    tail = rope[rope_len - 1]
    prev.add(tail)

    for instruction in instructions:
        direction, amt = instruction
        if direction == 'R':
            rope = move_rope(rope, amt, prev, 1, 0, rope_len)
        elif direction == 'L':
            rope = move_rope(rope, amt, prev, -1, 0, rope_len)
        elif direction == 'U':
            rope = move_rope(rope, amt, prev, 0, 1, rope_len)
        elif direction == 'D':
            rope = move_rope(rope, amt, prev, 0, -1, rope_len)
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
