from network_computer import NetworkComputer

def part1():
    computers = list(map(lambda address: NetworkComputer(address), range(0, 50)))
    while True:
        for computer in computers:
            packet = computer.step()
            if packet:
                if packet[0] == 255:
                    print('DONE!: ', packet)
                    return
                address = packet[0]
                print('Packet: ', packet)
                computers[address].send_packet(packet[1:])

# part1() 20665
