import string


def main():
    # https://adventofcode.com/2022/day/3
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    sacks = parse_file(lines)
    # print(sacks)

    scoring_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    print(scoring_list)

    score = 0
    for sack in sacks:
        score += score_sack(sack, scoring_list)
    print(score)

    print("Done!")


def score_sack(sack, scoring_list):
    left, right = sack
    shared = set(left).intersection(set(right))
    value = shared.pop()
    return scoring_list.index(value) + 1


def parse_file(lines):
    sacks = []
    for line in lines:
        line = line.strip()
        vals = list(line)
        middle = len(vals) // 2
        left = vals[0:middle]
        right = vals[middle:]
        sacks.append((left, right))

    return sacks


if __name__ == '__main__':
    main()
