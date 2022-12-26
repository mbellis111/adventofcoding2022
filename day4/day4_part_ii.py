
def main():
    # https://adventofcode.com/2022/day/4
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    pairs = parse_file(lines)
    # print(pairs)

    count = 0
    for pair in pairs:
        if check_overlaps(pair):
            count += 1
    print(count)

    print("Done!")


def check_overlaps(pair):
    left, right = pair
    ls, le = left
    rs, re = right
    # check if one range overlaps the other
    if ls <= rs and rs <= le:
        return True
    elif rs <= ls and ls <= re:
        return True
    return False

def parse_file(lines):
    pairs = []
    for line in lines:
        line = line.strip()
        left, right = line.split(",")
        ls, le = left.strip().split('-')
        rs, re = right.strip().split('-')
        pairs.append(((int(ls), int(le)), ( int(rs), int(re))))
    return pairs


if __name__ == '__main__':
    main()
