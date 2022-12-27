

def main():
    # https://adventofcode.com/2022/day/8
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    # create the dir tree structure
    matrix = parse_file(lines)
    # for row in matrix:
    #     print(row)

    count = count_visible(matrix)
    print(count)

    print("Done!")


def count_visible(matrix):
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if check_visible(matrix, r, c):
                count += 1
    return count


def check_visible(matrix, row, col):
    m_width = len(matrix)
    m_height = len(matrix[row])
    # if it's on the edge, its visible
    if row == 0 or col == 0 or row == m_width - 1 or col == m_height - 1:
        return True

    # only visible if all trees in ANY direction are less
    tree = matrix[row][col]

    # left
    visible = True
    for r in range(0, row):
        if matrix[r][col] >= tree:
            visible = False
            break
    if visible:
        return True

    # right
    visible = True
    for r in range(row + 1, m_width):
        if matrix[r][col] >= tree:
            visible = False
            break
    if visible:
        return True

    # up
    visible = True
    for c in range(0, col):
        if matrix[row][c] >= tree:
            visible = False
            break
    if visible:
        return True

    # down
    visible = True
    for c in range(col + 1, m_height):
        if matrix[row][c] >= tree:
            visible = False
            break
    if visible:
        return True

    return False


def parse_file(lines):
    matrix = []
    for line in lines:
        vals = [int(val) for val in list(line.strip())]
        matrix.append(vals)
    return matrix


if __name__ == '__main__':
    main()
