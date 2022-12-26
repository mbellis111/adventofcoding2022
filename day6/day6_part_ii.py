
def main():
    # https://adventofcode.com/2022/day/6
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    data = parse_file(lines)
    # print(data)

    index = find_unique_segment(data)
    print(index)

    print("Done!")


def find_unique_segment(data):
    si = 0
    ei = 14
    while ei < len(data):
        segment = data[si:ei]
        if len(set(segment)) == 14:
            return ei
        # increment by a character
        si += 1
        ei += 1
    return None

def parse_file(lines):
    data = lines[0].strip()
    return data


if __name__ == '__main__':
    main()
