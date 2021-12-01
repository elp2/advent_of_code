import sys
sys.path.append('..')

from intcode.intcode import IntCodeComputer


class NetworkComputer:
    def __init__(self, address):
        self.ic = IntCodeComputer(list(map(lambda m: int(m), open('input').readline().split(','))), [address])
        self.ic.debugging = False
        self.ate_negative_1 = False
        self.hungry = False

    def send_packet(self, packet):
        """Sends the computer a packet."""
        assert len(packet) == 2
        if self.ic.inputs == [-1]:
            self.ic.inputs = []
        self.ic.inputs += packet
        self.hungry = False

    def step(self):
        """Steps the computer. Returns an [address, x, y] packet or None if none."""
        assert self.ic.halted == False
        if len(self.ic.inputs) == 0:
            # Either finished or ate a -1 last time.
            self.ic.inputs = [-1]
        input_is_negative_1 = self.ic.inputs == [-1]
        self.ic.step()
        if input_is_negative_1:
            self.hungry = self.hungry or len(self.ic.inputs) == 0
        if len(self.ic.outputs) == 3:
            address_packet = self.ic.outputs
            self.ic.outputs = []
            return address_packet
        return None

    def is_halted(self):
        return self.ic.halted

    def is_hungry(self):
        return self.hungry
