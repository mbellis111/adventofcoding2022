

def main():
    # https://adventofcode.com/2022/day/8
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    # create the dir tree structure
    matrix = parse_file(lines)
    for row in matrix:
        print(row)

    score = get_best_score(matrix)
    print(score)

    print("Done!")


def get_best_score(matrix):
    largest = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            largest = max(get_view_score(matrix, r, c), largest)
    return largest


def get_view_score(matrix, row, col):
    m_width = len(matrix)
    m_height = len(matrix[row])
    # if it's on the edge, zero score
    if row == 0 or col == 0 or row == m_width - 1 or col == m_height - 1:
        return 0

    # score is the number of trees we can see from ours
    tree = matrix[row][col]

    # left
    left_score = 0
    for r in range(row - 1, -1, -1):
        left_score += 1
        if matrix[r][col] >= tree:
            break

    # right
    right_score = 0
    for r in range(row + 1, m_width):
        right_score += 1
        if matrix[r][col] >= tree:
            break
    # up
    up_score = 0
    for c in range(col - 1, -1, -1):
        up_score += 1
        if matrix[row][c] >= tree:
            break

    # down
    down_score = 0
    for c in range(col + 1, m_height):
        down_score += 1
        if matrix[row][c] >= tree:
            break

    # print(row, col, ":", left_score, right_score, up_score, down_score)

    return left_score * right_score * up_score * down_score


def parse_file(lines):
    matrix = []
    for line in lines:
        vals = [int(val) for val in list(line.strip())]
        matrix.append(vals)
    return matrix


if __name__ == '__main__':
    main()
