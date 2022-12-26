def main():
    # https://adventofcode.com/2022/day/1
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    values = parse_file(lines)
    # print(values)

    max_value = -1
    max_elf = None
    for elf in values:
        if elf["total"] > max_value:
            max_value = elf["total"]
            max_elf = elf

    print(max_elf)

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
