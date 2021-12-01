from collections import defaultdict

def return_default():
    return 0

REAL=open("18.txt").readlines()
SAMPLE=open("18.sample").readlines()

OPEN="."
TREE="|"
LUMBERYARD="#"

import copy

def safe_grid_get(grid, x, y, missing=None):
    if x < 0 or y < 0:
        return missing
    if y >= len(grid):
        return missing
    if x >= len(grid[y]):
        return missing
    return grid[y][x]


def parse_lines(lines):
    return list(map(lambda l: list(l.strip()), lines))


def next_sq(grid, x, y):
    around = defaultdict(return_default)
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            a = safe_grid_get(grid, x + dx, y + dy)
            if a is not None:
                around[a] += 1
    here = grid[y][x]
    if here == OPEN:
        if around[TREE] >= 3:
            return TREE
        else:
            return OPEN
    elif here == TREE:
        if around[LUMBERYARD] >= 3:
            return LUMBERYARD
        else:
            return TREE
    else:
        assert here == LUMBERYARD
        if around[LUMBERYARD] >= 1 and around[TREE] >= 1:
            return LUMBERYARD
        else:
            return OPEN


def resource_value(board):
    lands = defaultdict(return_default)
    for y in range(len(board)):
        for x in range(len(board[0])):
            lands[board[y][x]] += 1
    return lands[TREE] * lands[LUMBERYARD]


def solve(lines, minutes):
    cache = {}
    old_board = parse_lines(lines)

    for minute in range(minutes):
        board = copy.deepcopy(old_board)
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x] = next_sq(old_board, x, y)
        old_board = board
        key = "\n".join(map(lambda r: "".join(r), board))
        # print(key)
        if key in cache:
            print(minute, cache[key])
        else:
            cache[key] = (minute, resource_value(board))
    return resource_value(board)
sample = solve(SAMPLE, 10)
assert sample == 1147
print("*** SAMPLE PASSED ***")

# print(solve(REAL, 10000))

loop = """598 570 191420
599 571 189168
600 572 185082
601 573 185227
602 574 185320
603 575 185790
604 576 186120
605 577 189956
606 578 190068
607 579 191080
608 580 190405 # too low
609 581 193795
610 582 190950
611 583 193569
612 584 194350
613 585 196308
614 586 195364
615 587 197911
616 588 199755
617 589 201144
618 590 201607
619 591 203580
620 592 201260
621 593 201950
622 594 200675 # TOO HIGH
623 595 202208
624 596 200151
625 597 198948
626 570 191420
627 571 189168
628 572 185082
629 573 185227
630 574 185320
631 575 185790
632 576 186120
633 577 189956
634 578 190068
635 579 191080
636 580 190405
637 581 193795"""

num = 1000000000
nmod = 28
for num in range(570, 638):
    print(num, (num - 570) % nmod + 570)

num = 1000000000 - 1
print(num, (num - 570) % nmod + 570 + nmod)