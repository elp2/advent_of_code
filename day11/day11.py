from hull_painting_robot import HullPaintingRobot

def part1():
    hpr = HullPaintingRobot()
    hpr.paint_until_halt()

# part1() # 2343

def part2():
    hpr = HullPaintingRobot(start_on_white=True)
    hpr.paint_until_halt()
    hpr.print_grid()

part2()