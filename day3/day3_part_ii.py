import string


def main():
    # https://adventofcode.com/2022/day/3
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    sacks = parse_file(lines)
    # print(sacks)
    groups = group_sacks(sacks)
    for group in groups:
        print(group)

    scoring_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    # print(scoring_list)

    score = 0
    for group in groups:
        score += score_group(group, scoring_list)
    print(score)

    print("Done!")


def score_group(group, scoring_list):
    first, second, third = group
    shared = set(first).intersection(set(second)).intersection(set(third))
    value = shared.pop()
    return scoring_list.index(value) + 1


def group_sacks(sacks):
    groups = []

    num = 0
    for i, sack in enumerate(sacks):
        num += 1
        if num == 3:
            groups.append((sacks[i-2], sacks[i-1], sacks[i]))
            num = 0

    return groups


def parse_file(lines):
    sacks = []
    for line in lines:
        line = line.strip()
        vals = list(line)
        sacks.append(vals)
    return sacks


if __name__ == '__main__':
    main()
