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
    if you == 'X':
        return 1
    elif you == 'Y':
        return 2
    elif you == 'Z':
        return 3
    return None

def score_win(opp, you):
    if opp == 'A':
        if you == 'X':
            return 3
        elif you == 'Y':
            return 6
        elif you == 'Z':
            return 0
    elif opp == 'B':
        if you == 'X':
            return 0
        elif you == 'Y':
            return 3
        elif you == 'Z':
            return 6
    elif opp == 'C':
        if you == 'X':
            return 6
        elif you == 'Y':
            return 0
        elif you == 'Z':
            return 3
    return None



def play_round(opp, you):
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock

    win_score = score_win(opp, you)
    play_score = score_play(you)
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
