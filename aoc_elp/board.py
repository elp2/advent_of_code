import os, sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

from aoc_elp.utils import CHAR_TO_DS

class Vel:
    def __init__(self, vx, vy):
        self.vx, self.vy = vx, vy
    
    def __repr__(self):
        return f"Vel({self.vx},{self.vy})"

def VelFromChar(char):
    vx, vy = CHAR_TO_DS[char]
    return Vel(vx, vy)


class Pos:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Pos({self.x},{self.y})"

    def step(self, v: Vel):
        self.x += v.vx
        self.y += v.vy
    
    def add(self, v: Vel):
        return Pos(x=self.x + v.vx, y=self.y + v.vy)

class Board:
    """A class for handling AOC grid problems.
    
    Works with the Pos and Vel classes."""

    def __init__(self, lines, mover_replace = None):
        self.board = []
        self.movers = []
        for y, row in enumerate(lines.split("\n")):
            row = list(row.strip())
            for x, char in enumerate(row):
                if None != mover_replace:
                    mover, replace = mover_replace
                    if char == mover:
                        self.movers.append(Pos(x, y))
                        row[x] = replace
            self.board.append(row)

        assert len(set([len(row) for row in self.board])) == 1

        self.width = len(self.board[0])
        self.height = len(self.board)

    def __getitem__(self, key):        
        return self.at(key.x, key.y, off_board=IndexError)
    
    def __setitem__(self, key, value):
        self.board[key.y][key.x] = value

    def mover(self) -> Pos:
        assert len(self.movers) == 1
        return self.movers[0]
    

    def valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height


    def at(self, x: int, y: int, off_board= IndexError) -> str:
        """Returns what is on the board at this position, ignoring movers.
        
        Args:
            off_board: Defines behavior for if (x, y) is off the board."""
        if not self.valid(x, y):
            if off_board == IndexError:
                raise IndexError
            else:
                return off_board
        return self.board[y][x]    

    def validpos(self, p: Pos) -> bool:
        return self.valid(p.x, p.y)

    def print_board(self, movers=None, mover_char="@"):
        if movers == None:
            movers = self.movers
        
        for y, row in enumerate(self.board):
            for m in movers:
                if m.y == y:
                    row = row[:]
                    row[m.x] = mover_char
            print("".join(row))

    def validate_board(self, mover_empty=None):
        for m in self.movers:
            assert self.valid(m.x, m.y)
            if mover_empty != None:
                assert self.at(m.x, m.y) in mover_empty


    def apply_transactions(self, transactions):
        for (opos, npos, (oat, nat)) in transactions:
            self[opos] = oat
        for (opos, npos, (oat, nat)) in transactions:
            self[npos] = nat
        