import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer

# Parsing modes.
TITLE = 'title'
DESCRIPTION = 'description'
DOORS = 'doors'
ITEMS = 'items'
COMMAND = 'command'

class Adventure:
    def __init__(self):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))), input_provider=lambda: self.input_provider())
        self.input = ''
        self.room_to_items = {}
        self.room_to_directions = {}
        self.paths = [[]]
    
    def manual_input_provider(self):
        while True:
            line = input('').strip()
            if len(line):
                # Inputs must end with a "\n" so add one.
                return list(map(lambda char: ord(char), line)) + [ord('\n')]
            else:
                print('No input!')

    def input_provider(self):
        assert len(self.input)
        print('Input: %s' % (self.input))
        ascii_list = list(map(lambda char: ord(char), self.input)) + [ord('\n')]
        self.input = ''
        return ascii_list

    def navigate_path(self, path):
        room = self.read_room()

        for dir in path:
            self.input = dir
            room = self.read_room()
        self.mark_visited(room, path)


    def explore_rooms(self):
        while True:
            path = self.paths[0]
            self.paths = self.paths[1:]
            self.navigate_path(path)

            if not len(self.paths):
                print(self.room_to_directions)
                print(self.room_to_items)
                return

    def play(self):
        path = []
        self.ic.input_provider = self.manual_input_provider
        while True:
            room = self.read_room()

    def mark_visited(self, room, path):
        if room[TITLE] in self.room_to_directions:
            # Already visited.
            return
        print('Visiting: %s' % (room[TITLE]))
        self.room_to_directions[room[TITLE]] = path
        self.room_to_items[room[TITLE]] = room[ITEMS]
        for door in room[DOORS]:
            self.paths.append(path[:] + [door])

    def input_for(self, room):
        return room[DOORS][0]

    def read_line(self):
        while len(self.ic.outputs) == 0 or chr(self.ic.outputs[-1]) != '\n':
            self.ic.step()
        line = ''.join(list(map(chr, self.ic.outputs))).strip()
        self.ic.outputs = []
        return line

    def read_room(self):
        mode = TITLE
        room = {'text': '', 'doors': [], 'items': []}
        while True:
            line = self.read_line()
            if None == line:
                return room
            room['text'] += line + '\n'
            if line.startswith('Command'):
                mode = COMMAND
            if mode == TITLE:
                if not len(line):
                    continue
                assert line.startswith('==')
                room[TITLE] = line[3:len(line) - 3]
                mode = DESCRIPTION
                room[DESCRIPTION] = ''
            elif mode == DESCRIPTION:
                if line.startswith('Doors'):
                    mode = DOORS
                else:
                    if len(line.strip()) > 0:
                        room[DESCRIPTION] += line
            elif mode == DOORS:
                if line.startswith('- '):
                    room[DOORS].append(line[2:])
                elif line.startswith('Items'):
                    mode = ITEMS
            elif mode == ITEMS:
                if line.startswith('- '):
                    room[ITEMS].append(line[2:])
                elif line.startswith('Command'):
                    mode = COMMAND
            elif mode == COMMAND:
                print(room)
                break
        return room


def part1():
    a = Adventure()
    a.explore_rooms()

if __name__ == "__main__":
    part1()