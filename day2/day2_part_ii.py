def main():
    # https://adventofcode.com/2022/day/2
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    theirs, yours = parse_file(lines)
    print(theirs)
    print(yours)

    score = 0
    for them, you in zip(theirs, yours):
        score += play_round(them, you)
    print(score)

    print("Done!")


def score_play(you):
    if you == 'A':
        return 1
    elif you == 'B':
        return 2
    elif you == 'C':
        return 3
    return None


def score_win(you):
    if you == 'X':
        return 0
    elif you == 'Y':
        return 3
    elif you == 'Z':
        return 6
    return None


def get_play(opp, you):
    # A for Rock, B for Paper, and C for Scissors
    # X = lose, Y = draw, and Z = win
    if opp == 'A':
        if you == 'X':
            return 'C'
        elif you == 'Y':
            return 'A'
        elif you == 'Z':
            return 'B'
    elif opp == 'B':
        if you == 'X':
            return 'A'
        elif you == 'Y':
            return 'B'
        elif you == 'Z':
            return 'C'
    elif opp == 'C':
        if you == 'X':
            return 'B'
        elif you == 'Y':
            return 'C'
        elif you == 'Z':
            return 'A'
    return None


def play_round(opp, you):
    # A for Rock, B for Paper, and C for Scissors
    # X = lose, Y = draw, and Z = win
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

    you_play = get_play(opp, you)
    win_score = score_win(you)
    play_score = score_play(you_play)
    return win_score + play_score


def parse_file(lines):
    theirs = []
    yours = []
    for line in lines:
        left, right = line.strip().split(" ")
        theirs.append(left.strip())
        yours.append(right.strip())
    return theirs, yours


if __name__ == '__main__':
    main()
