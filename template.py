
def main():
    # https://adventofcode.com/2022/day/X
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    data = parse_file(lines)
    print(data)

    print("Done!")


def parse_file(lines):
    data = []
    for line in lines:
        data.append(line)
    return data


if __name__ == '__main__':
    main()
