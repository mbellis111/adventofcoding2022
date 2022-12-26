
def main():
    # https://adventofcode.com/2022/day/4
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    pairs = parse_file(lines)
    # print(pairs)

    count = 0
    for pair in pairs:
        if check_contained(pair):
            count += 1
    print(count)

    print("Done!")


def check_contained(pair):
    left, right = pair
    ls, le = left
    rs, re = right
    # check if one range contains the other
    if ls <= rs and le >= re:
        return True
    elif rs <= ls and re >= le:
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
