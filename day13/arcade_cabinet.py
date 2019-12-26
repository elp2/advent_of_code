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

def tile_to_string(tile):
    if tile == EMPTY:
        return ' '
    elif tile == WALL:
        return '*'
    elif tile == BLOCK:
        return '_'
    elif tile == PADDLE:
        return 'V'
    elif tile == BALL:
        return 'B'
    else:
        assert False

class ArcadeCabinet:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
        self.clear_screen()
        self.ball_velocity = [1, 1]
        self.ball_pos = None # Update in first time we see it.

    def clear_screen(self):
        self.screen = []
        for y in range(0, 22):
            self.screen.append([EMPTY] * 40)
        self.score = 0

    def play(self):
        memory = list(map(lambda m: int(m), open('input').readline().split(',')))
        # Play for free.
        memory[0] = 2
        self.ic = IntCodeComputer(memory)

        while True:
            self.game_loop()

    def game_loop(self):
        while self.ic.next_opcode() != 3:
            self.ic.step()
            if len(self.ic.outputs) == 3:
                [x, y, tile] = self.ic.outputs
                self.ic.outputs = []
                self.add_tile(x, y, tile)

        self.print_screen()
        self.ai_play()
        self.ic.step()
        assert len(self.ic.inputs) == 0

    def add_tile(self, x, y, tile):
        if -1 == x:
            assert y == 0
            self.score = tile
        else:
            self.screen[y][x] = tile

    def print_screen(self):
        print('SCORE: %d' % (self.score))

        num_blocks = 0
        for y in range(0, len(self.screen)):
            line = ''
            for x in range(0, len(self.screen[y])):
                tile = self.screen[y][x]
                if tile == BLOCK:
                    num_blocks += 1
                elif tile == BALL:
                    if self.ball_pos == None:
                        self.ball_pos = (x, y)
                        self.ball_velocity = (1, 1)
                    else:
                        old = self.ball_pos
                        self.ball_velocity = (x - old[0], y - old[1])
                        self.ball_pos = (x, y)

                elif tile == PADDLE:
                    self.paddle_pos = (x, y)
                line += tile_to_string(tile)
            print(line)
        
        if num_blocks == 0:
            print('Destroyed all blocks! Final score: %d' % (self.score))
            sys.exit(0)

    def ball_intersecction_x(self, steps):
        """Returns x if ball intersects paddle within [steps] otherwise None."""
        paddle_y = self.paddle_pos[1] - 1
        ball_velocity = self.ball_velocity
        ball_pos = self.ball_pos
        # assert > ball_pos[1], 'Ball at paddle, YOU LOSE!'
        screen = self.screen[:]
        if ball_pos[1] == paddle_y:
            return ball_pos[0]
        path = []
        while steps != 0:
            next = (ball_pos[0] + ball_velocity[0], ball_pos[1] + ball_velocity[1])
            if next[1] == paddle_y:
                return next[0]
            elif next[1] == paddle_y + 1:
                assert False, 'YOU LOSE!'
            tile = screen[next[1]][next[0]]

            while True:
                [bx, by] = ball_pos
                [vx, vy] = ball_velocity
                hit_block = False
                if screen[by][bx + vx] == BLOCK:
                    screen[by][bx + vx] = EMPTY
                    vx *= -1
                    hit_block = True
                elif screen[by + vy][bx] == BLOCK:
                    screen[by + vy][bx] = EMPTY
                    vy *= -1
                    hit_block = True
                if not hit_block:
                    break

            tile = screen[next[1]][next[0]]
            if tile == WALL:
                ball_velocity = (-1 * ball_velocity[0], ball_velocity[1])
                next = (ball_pos[0] + ball_velocity[0], ball_pos[1] + ball_velocity[1])
            path.append(next)
            ball_pos = next
            steps -= 1
        print('No intersection following %s' % (path))
        if self.ball_pos[0] > self.paddle_pos[0]:
            return 1
        elif elf.ball_pos[0] > self.paddle_pos[0]:
            return -1
        return None

    def ai_play(self):
        """Move the paddle to where the ball will be."""
        intersection = self.ball_intersecction_x(15)
        if intersection == None:
            print('HOLD')
            move = 0
        elif intersection == self.paddle_pos[0]:
            print('_')
            move = 0
        elif intersection > self.paddle_pos[0]:
            print('>')
            move = 1
        elif intersection < self.paddle_pos[0]:
            print('<')
            move = -1
        assert len(self.ic.inputs) == 0
        self.ic.inputs = [move]
