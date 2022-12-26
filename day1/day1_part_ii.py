def main():
    # https://adventofcode.com/2022/day/1
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    values = parse_file(lines)
    # print(values)

    # sort by total
    values = sorted(values, key=lambda d: d['total'], reverse=True)
    print(values)

    total_cals = 0
    for i in range(0, 3):
        if i < len(values):
            total_cals += values[i]["total"]
    print(total_cals)

    print("Done!")


def parse_file(lines):
    elves = []
    elf = []
    for line in lines:
        line = line.strip()
        if not line or len(line) == 0:
            total = sum(elf)
            elves.append({
                "total": total,
                "values": elf
            })
            elf = []
        else:
            elf.append(int(line))
    return elves


if __name__ == '__main__':
    main()
