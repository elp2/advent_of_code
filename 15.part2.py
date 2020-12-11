from collections import defaultdict
import queue
import copy

def return_default():
    return 0

def dd():
    return defaultdict(return_default)

def abround(x, y, board):
    poss = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    ret = []
    for px, py in poss:
        if not (0 <= py <= len(board)) or not (0 <= px <= len(board[y])):
            continue
        ret.append((px, py))
    return ret


def get_fighter_positions(fighters):
    fighter_pos = set()
    for f in fighters:
        if not f.dead():
            fighter_pos.add((f.x, f.y))
    return fighter_pos


def find_all_paths(x, y, fighters, board):
    fighter_poses = get_fighter_positions(fighters)
    fastest = {}
    q = queue.Queue()
    q.put(((x, y), []))
    while not q.empty():
        (x, y), path = q.get()
        pos = (x, y)

        # Already found here? This route needs to be faster.
        if pos in fastest:
            prev_fastest = fastest[pos]
            if len(path) >= len(prev_fastest):
                continue
        assert board[y][x] != "#"
        fastest[pos] = path
        for a in abround(x, y, board):
            ax, ay = a
            if board[ay][ax] == "#" or a in fighter_poses:
                continue
            q.put((a, path + [a]))
    return fastest

    # Find paths to everywhere
    # Find paths to all spaces abround enemies
    # Find shortest path to enemy
    # return that.

class Fighter:
    def __init__(self, team, x, y, hp=200, attack=3):
        self.team = team
        self.x = x
        self.y = y
        self.hp = hp
        self.attack = attack
    

    def dead(self):
        return self.hp <= 0


    def damage(self, hp):
        self.hp -= hp
        if self.hp < 0:
            print(self.x, self.y, self.team, self.hp, "DEAD!")

    def sorted_enemies(self, fighters):
        eteam = {"E": "G", "G": "E"}[self.team]
        enemies = find_teams(fighters)[eteam]
        enemies.sort(key=lambda e: e.y * 10000 + e.x)
        return enemies

    def draw_board(self, fighters, orig_board):
        board = copy.deepcopy(orig_board)
        for f in fighters:
            if f == self:
                c = self.team.lower()
            else:
                c = f.team
            board[f.y][f.x] = c
        print("\n".join(map(lambda l: "".join(l), board)))

    def attack_abround(self, fighters, board):
        sorted_enemies = self.sorted_enemies(fighters)
        enemies = []
        for a in abround(self.x, self.y, board):
            for f in sorted_enemies:
                if f == self or f.dead() or f.team == self.team:
                    continue
                if f.x == a[0] and f.y == a[1]:
                    enemies.append(f)
        if not enemies:
            return False
        min_hp = min(list(map(lambda f: f.hp, enemies)))
        for e in enemies:
            if e.hp == min_hp:
                # print(self.team, self.x, self.y, " damages, : ", e.x, e.y)
                e.damage(self.attack)
                return True


        return False


    def action(self, fighters, board):
        # Attack adjacent.
        if self.attack_abround(fighters, board):
            return
        
        # Nothing adjacent, move.
        paths = find_all_paths(self.x, self.y, fighters, board)
        enemies = self.sorted_enemies(fighters)
        adjacents = set()
        for e in enemies:
            for ax, ay in abround(e.x, e.y, board):
                adjacents.add((ax, ay))
        adjacents = list(adjacents)
        adjacents.sort(key=lambda a: a[1] * 10000 + a[0])

        min_len = None
        target = None
        for a in adjacents:
            # TODO - path not available?
            if a not in paths:
                continue
            apath = paths[a]
            if min_len is None or len(apath) < min_len:
                min_len = len(apath)
                target = apath[0]
        if target == None:
            # Nowhere to move.
            # print("staying at ", self.x, self.y)
            return
        tx, ty = target
        # print(self.team, self.x, self.y, " moves, : ", tx, ty)
        assert board[ty][tx] == "." and (tx, ty) != (self.x, self.y)
        self.x, self.y = target

        # After moving (or if the unit began its turn in range of a target), the unit attacks.
        self.attack_abround(fighters, board)

CHALLENGE_DAY = "15"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample").read()
SAMPLE_EXPECTED = 4988
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    # return split
    # return list(map(int, lines))
    return list(map(lambda l: list(l.strip()), split)) # beware leading / trailing WS


def find_fighters(parsed, elf_attack):
    fighters = []
    for y in range(len(parsed)):
        for x in range(len(parsed[y])):
            here = parsed[y][x]
            if here in "GE":
                if here == "E":
                    attack = elf_attack
                else:
                    attack = 3
                fighters.append(Fighter(here, x, y, 200, attack=attack))
                parsed[y][x] = "."
    return fighters


def find_teams(fighters):
    ret = {"G": [], "E": []}
    for f in fighters:
        if not f.dead():
            ret[f.team].append(f)
    return ret


def run_battle(elf_attack, board):
    # print("Elf attack -> ", elf_attack)
    fighters = find_fighters(board, elf_attack)
    bround = 0
    while True:
        bround_finished = run_bround(fighters, board)
        if bround_finished:
            if elves_won(fighters):
                elf_fighters = find_teams(fighters)["E"]
                elf_fighters[0].draw_board(elf_fighters, board)
                for tf in elf_fighters:
                    print (tf.team, tf.hp)
                return (fighters, bround)
            else:
                return None
        bround += 1
    



def run_bround(fighters, board):
    # units take their turns within a bround is the reading order of their starting positions in that bround
    turn_fighters = [f for f in fighters if not f.dead()]
    turn_fighters.sort(key=lambda f: f.y * 100000 + f.x)

    # print("\nAfter ", bround, "bround(s):")
    if not turn_fighters:
        return True
    # turn_fighters[0].draw_board(turn_fighters, board)
    # for tf in turn_fighters:
    #     print (tf.team, tf.hp)
    teams = find_teams(turn_fighters)
    if not teams["G"] or not teams["E"]:
        assert True
    
    for f in turn_fighters:
        # Each unit begins its turn by identifying all possible targets (enemy units). If no targets remain, combat ends.
        teams = find_teams(turn_fighters)
        if not teams["G"] or not teams["E"]:
            return True

        if f.dead():
            continue
        fighters = [f for f in fighters if not f.dead()]
        fighters.sort(key=lambda f: f.y * 100000 + f.x)
        f.action(fighters, board)
        fighters = [f for f in fighters if not f.dead()]
        fighters.sort(key=lambda f: f.y * 100000 + f.x)
    return False

def find_winners(fighters, bround):
    teams = find_teams(fighters)
    if teams["G"]:
        winners = teams["G"]
        assert False
    else:
        winners = teams["E"]
    hps = []
    winners.sort(key=lambda f: f.y * 100000 + f.x)
    for w in winners:
        hps.append(w.hp)
    sumhp = sum(hps)
    print("Winners: ", bround, hps, sumhp)
    return bround * sumhp


def elves_won(fighters):
    teams = find_teams(fighters)
    if teams["E"]:
        return True
    else:
        return False



def solve(raw):
    board = parse_lines(raw)

    elf_attack = 3
    while True:
        print("Battling at ", elf_attack)
        battle = run_battle(elf_attack, copy.deepcopy(board))
        if battle:
            fighters, bbround = battle
            print("WIN AT rpimd: ", bbround, "attack: ", elf_attack)
            return find_winners(fighters, bbround)
        else:
            elf_attack += 1

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

# SAMPLE2 = open(CHALLENGE_DAY + ".sample2").read()
# sample2 = solve(SAMPLE2)
# print(sample2)
# assert sample2 == 36334


solved = solve(REAL)
print("SOLUTION: ", solved) # 191232 (TOO High. Passes sample though) # 188576!
# 23180 too low
# assert solved