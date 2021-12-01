from copy import deepcopy

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
BALL_MOTION = 5

def tile_to_string(tile):
    if tile == EMPTY:
        return ' '
    elif tile == WALL:
        return '*'
    elif tile == BLOCK:
        return '*'
    elif tile == PADDLE:
        return 'V'
    elif tile == BALL:
        return 'B'
    elif tile == BALL_MOTION:
        return 'b'
    else:
        assert False

class ArcadeCabinet:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))))
        self.clear_screen()
        self.ball_velocity = [1, 1]
        self.ball_pos = None # Update in first time we see it.
        self.expected_ball_pos = None
        self.last_score = None
        self.board_history = [1,2,3]
        self.steps = 0

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
        if self.last_score != self.score:
            print('SCORE: %d' % (self.score))
            self.last_score = self.score
        self.board_history[self.steps % 3] = self.stringify(self.screen)
        self.steps += 1
        self.read_state()
        self.ai_play()
        self.ic.step()
        assert len(self.ic.inputs) == 0

    def add_tile(self, x, y, tile):
        if -1 == x:
            assert y == 0
            self.score = tile
        else:
            self.screen[y][x] = tile

    def read_state(self):
        num_blocks = 0
        for y in range(0, len(self.screen)):
            for x in range(0, len(self.screen[y])):
                tile = self.screen[y][x]
                if tile == BALL:
                    if self.ball_pos == None:
                        self.ball_pos = (x, y)
                        self.ball_velocity = (1, 1)
                    else:
                        old = self.ball_pos
                        self.ball_velocity = (x - old[0], y - old[1])
                        self.ball_pos = (x, y)
                        if self.expected_ball_pos and self.expected_ball_pos != self.ball_pos:
                            (ex, ey) = self.expected_ball_pos
                            screen = deepcopy(self.screen)
                            screen[ey][ex] = BALL_MOTION
                            print(self.stringify(screen))
                            print('Velocity:', self.ball_velocity)
                            i = self.steps % 3
                            print(self.board_history[i - 2])
                            print(self.board_history[i - 3])
                            # assert False, 'Unexpected ball position!'
                elif tile == PADDLE:
                    self.paddle_pos = (x, y)
                elif tile == BLOCK:
                    num_blocks += 1

        if num_blocks == 0:
            print('Destroyed all blocks! Final score: %d' % (self.score))
            sys.exit(0)


    def ball_intersection_x(self, steps):
        """Returns x if ball intersects paddle within [steps] otherwise None."""
        intersection_y = self.paddle_pos[1] - 1

        screen = deepcopy(self.screen)
        path = []

        [vx, vy] = self.ball_velocity
        [bx, by] = self.ball_pos
        assert by <= intersection_y, 'MISSED BALL!'
        while steps != 0:
            path.append((bx, by))
            if by == intersection_y:
                break

            loop = 5
            while True:
                loop -= 1
                if loop == 0:
                    print('loop=0?')
                nx = bx + vx
                ny = by + vy
                block_x = screen[by][nx] == BLOCK
                block_y = screen[ny][bx] == BLOCK
                if block_x and block_y:
                    screen[ny][bx] = EMPTY
                    vy *= -1
                    screen[by][nx] = EMPTY
                    vx *= -1
                elif block_y:
                    screen[ny][bx] = EMPTY
                    vy *= -1
                elif block_x:
                    screen[by][nx] = EMPTY
                    vy *= -1
                elif screen[ny][bx] == WALL:
                    vy *= -1
                elif screen[by][nx] == WALL:
                    vx *= -1
                elif screen[ny][nx] == EMPTY or screen[ny][nx] == BALL:
                    break
                elif screen[ny][nx] == BLOCK:
                    screen[ny][nx] = EMPTY
                    vx *= -1
                    vy *= -1

            assert abs(bx - nx) == 1
            assert abs(by - ny) == 1
            bx = nx
            by = ny
            steps -= 1

        if path[-1][1] == intersection_y:
            if len(path) > 1:
                self.expected_ball_pos = path[1]
            else:
                self.expected_ball_pos = None

            return path[-1][0]
        else:
            # print('No intersection following %s' % (path))
            # for p in path:
            #     screen[p[1]][p[0]] = BALL_MOTION
            # print(self.stringify(screen))
            # assert False
            return None

    def stringify(self, screen):
        ret = ''
        for y in range(0, len(screen)):
            line = ''
            for x in range(0, len(screen[y])):
                line += tile_to_string(screen[y][x])
            ret += line + '\n'
        return ret

    def ai_play(self):
        """Move the paddle to where the ball will be."""
        intersection = self.ball_intersection_x(2000)
        if intersection == None:
            move = 0
        elif intersection == self.paddle_pos[0]:
            move = 0
        elif intersection > self.paddle_pos[0]:
            move = 1
        elif intersection < self.paddle_pos[0]:
            move = -1
        assert len(self.ic.inputs) == 0
        self.ic.inputs = [move]

def part2():
    ac = ArcadeCabinet()
    ac.play()

if __name__ == "__main__":
    part2()