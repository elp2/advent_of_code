import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

# 0 is an empty tile. No game object appears in this tile.
EMPTY = 0
# 1 is a wall tile. Walls are indestructible barriers.
WALL = 1
# 2 is a block tile. Blocks can be broken by the ball.
BLOCK = 2
# 3 is a horizontal paddle tile. The paddle is indestructible.
PADDLE = 3
# 4 is a ball tile. The ball moves diagonally and bounces off objects.
BALL = 4

class ArcadeCabinet:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
        self.screen = {}

    def count_block_tiles(self):
        while self.ic.halted == False:
            while len(self.ic.outputs) != 3:
                self.ic.step()
            
            [x, y, tile] = self.ic.outputs
            self.ic.outputs = []
            
            if (x,y) in self.screen:
                print('Already have %d at %s before %d' % (self.screen[(x,y)], (x,y), tile))
            self.screen[(x,y)] = tile

        return list(self.screen.values()).count(BLOCK)