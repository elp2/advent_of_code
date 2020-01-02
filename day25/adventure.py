import sys
sys.path.append('..')
from intcode.intcode import IntCodeComputer
from itertools import product

# Parsing modes.
TITLE = 'title'
DESCRIPTION = 'description'
DOORS = 'doors'
ITEMS = 'items'
COMMAND = 'command'

ROOM_PATHS = {'Hull Breach': [], 'Storage': ['east'], 'Gift Wrapping Center': ['south'], 'Navigation': ['west'], 'Holodeck': ['south', 'east'], 'Hallway': ['south', 'west'], 'Hot Chocolate Fountain': ['south', 'east', 'east'], 'Passages': ['south', 'east', 'south'], 'Crew Quarters': ['south', 'west', 'north'], 'Stables': ['south', 'east', 'east', 'east'], 'Engineering': ['south', 'east', 'east', 'south'], 'Warp Drive Maintenance': ['south', 'east', 'south', 'east'], 'Science Lab': ['south', 'east', 'south', 'south'], 'Corridor': ['south', 'east', 'east', 'east', 'east'], 'Sick Bay': ['south', 'east', 'south', 'east', 'east'], 'Observatory': ['south', 'east', 'south', 'south', 'east'], 'Arcade': ['south', 'east', 'south', 'south', 'west'], 'Kitchen': ['south', 'east', 'south', 'south', 'west', 'south'], 'Security Checkpoint': ['south', 'east', 'south', 'south', 'west', 'south', 'west'], 'Pressure-Sensitive Floor': ['south', 'east', 'south', 'south', 'west', 'south', 'west', 'west']}
ITEM_PER_ROOM = {'Hull Breach': [], 'Storage': [], 'Gift Wrapping Center': ['photons'], 'Navigation': ['whirled peas'], 'Holodeck': ['mutex'], 'Hallway': ['bowl of rice'], 'Hot Chocolate Fountain': ['astronaut ice cream'], 'Passages': ['escape pod'], 'Crew Quarters': [], 'Stables': ['ornament'], 'Engineering': ['tambourine'], 'Warp Drive Maintenance': ['mug'], 'Science Lab': ['molten lava'], 'Corridor': ['infinite loop'], 'Sick Bay': [], 'Observatory': [], 'Arcade': ['giant electromagnet'], 'Kitchen': ['easter egg'], 'Security Checkpoint': [], 'Pressure-Sensitive Floor': []}

class Adventure:
    def __init__(self, manual=False):
        input_provider = lambda: self.provide_input(manual)
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))), input_provider=input_provider)
        self.input = ''
        self.room_to_items = {}
        self.room_to_directions = {}
        self.paths = []
        self.all_paths = []
        self.debugging = False
        self.good_items = {}
    
    def provide_input(self, manual):
        if manual:
            return self.manual_input_provider()
        else:
            return self.input_provider()

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
        for dir in path:
            self.input = dir
            room = self.read_room()
        return room

    def reverse_path(self, path):
        path = path[:]
        path.reverse()
        REVERSE = {'north': 'south', 'east': 'west', 'west': 'east', 'south': 'north'}
        for dir in path:
            reversed = REVERSE[dir]
            self.input = reversed
            room = self.read_room()
        if self.debugging:
            print('Reversed path: %s' % (path))
        return room

    def explore_rooms(self):
        origin = self.read_room()
        self.mark_visited(origin, [])
        while len(self.paths):
            path = self.paths[0]
            self.paths = self.paths[1:]
            room = self.navigate_path(path)
            self.mark_visited(room, path)
            returned = self.reverse_path(path)
            assert returned == origin
            if self.debugging:
                print('Navigated to %s via path %s' % (room[TITLE], path))
        print('Finished exploring.')
        print(self.room_to_directions)
        print(self.room_to_items)

    def play(self):
        self.explore_rooms()

    def mark_visited(self, room, path):
        if room[TITLE] in self.room_to_directions:
            assert len(path) >= len(self.room_to_directions[room[TITLE]])
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
                # assert line.startswith('==')
                if not line.startswith('=='):
                    print('Non title: ' + line)
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
                # print('At: %s ' % (room))
                break
        return room

    def get_all_items(self):
        origin = self.read_room()

        bad_items = {'photons': 'grue', 'escape pod': 'launched into space', 'molten lava': 'you melt', 'infinite loop': 'infinite loop', 'giant electromagnet': 'get stuck'}

        for room, items in ITEM_PER_ROOM.items():
            if len(items) and items[0] not in bad_items:
                path = ROOM_PATHS[room]
                print('Looking for %s in %s follwing %s' % (items, room, path))
                at = self.navigate_path(path)
                assert at[ITEMS] == items
                for item in items:
                    if item not in bad_items:
                        self.take_item(item)
                        self.good_items[item] = True
                returned = self.reverse_path(path)
                assert origin == returned

    def take_item(self, name):
        self.input = 'take ' + name
        result = self.read_line() + '\n' + self.read_line() + self.read_line() + '\n' + self.read_line() + '\n'
        assert result == '\nYou take the ' + name + '.\nCommand?\n'
    
    def leave_items_in_security(self):
        path = ROOM_PATHS['Security Checkpoint']
        checkpoint = self.navigate_path(path)
        assert checkpoint[TITLE] == 'Security Checkpoint'
        print(checkpoint)
        for item in self.good_items.keys():
            self.drop_item(item)

    def drop_item(self, name):
        self.input = 'drop ' + name
        result = self.read_line() + '\n' + self.read_line() + self.read_line() + '\n' + self.read_line() + '\n'
        assert result == '\nYou drop the ' +  name + '.\nCommand?\n'

    def go_past_floor(self):
        items = list(self.good_items.keys())
        for combo in product([False, True], repeat=len(items)):
            brought = []
            for i in range(0, len(items)):
                if combo[i]:
                    self.take_item(items[i])
                    brought.append(items[i])
            self.input = 'west'

            # 1 real answer is heaver, -1 lighter
            weight_delta = 0
            lines = ''

            while True:
                line = self.read_line()
                if 'lighter than the detected value' in line:
                    weight_delta = -1
                elif 'heavier than the detected value' in line:
                    weight_delta = 1
                lines += line + '\n'
                if line == 'Command?':
                    break
            if 0 == weight_delta:
                print(lines)
                print("!!!!!!! with %s" % (brought))
            else:
                print('*** %s weight: %d' % (brought, weight_delta))

            for b in brought:
                self.drop_item(b)

def part1():
    # a = Adventure()
    # a.explore_rooms()
    a = Adventure()
    a.get_all_items()
    a.leave_items_in_security()
    a.go_past_floor()
    # Input: take mutex
    # Input: take astronaut ice cream
    # Input: take tambourine
    # Input: take easter egg
    # 295944

def manual():
    a = Adventure(manual=True)
    while True:
        line = a.read_line()
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        manual()
    else:
        part1()
    # manual()