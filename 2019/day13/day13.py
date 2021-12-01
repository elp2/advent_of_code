from arcade_cabinet import ArcadeCabinet

def part1():
    ac = ArcadeCabinet()
    print(ac.count_block_tiles())

# Doesn't work exactly anymore after I changed the arcade_cabinet to loop mode.
# part1() # 247

def part2():
    ac = ArcadeCabinet()
    ac.play()

part2()