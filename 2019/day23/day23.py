from network_computer import NetworkComputer

import sys

def part2():
    computers = list(map(lambda address: NetworkComputer(address), range(0, 50)))
    nat_packet = None
    last_nat_y = None

    sent_packets = 0
    while True:
        hungry_computers = []
        for i, computer in enumerate(computers):
            packet = computer.step()
            if computer.is_hungry():
                hungry_computers.append(i)
            if packet:
                sent_packets += 1
                address = packet[0]
                packet_contents = packet[1:]

                print('Packet #%d: %s' % (sent_packets, packet))
                if address == 255:
                    nat_packet = packet_contents
                    assert len(nat_packet) == 2

                else:
                    computers[address].send_packet(packet_contents)
        # print(len(hungry_computers))
        if len(hungry_computers) == 50 and sent_packets > 0:
            assert nat_packet
            print('Sending NAT packet')
            computers[0].send_packet(nat_packet)

            if last_nat_y == nat_packet[1]:
                print('Sent %d to NAT 2x' % (last_nat_y))
                sys.exit()
            last_nat_y = nat_packet[1]

            nat_packet = None

part2() # 13358
