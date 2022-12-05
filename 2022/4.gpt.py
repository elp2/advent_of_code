import sys


class Range:
    def __init__(self, range_str):
        self.start, self.end = map(int, range_str.split("-"))

    def contains(self, other):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other):
        return self.start <= other.end and self.end >= other.start


def count_fully_contained_pairs(range_strs):
    ranges = [Range(range_str) for range_str in range_strs]
    count = 0
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if ranges[i].contains(ranges[j]):
                count += 1
            elif ranges[j].contains(ranges[i]):
                count += 1
    return count


def count_overlapping_pairs(range_strs):
    ranges = [Range(range_str) for range_str in range_strs]
    count = 0
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if ranges[i].overlaps(ranges[j]):
                count += 1
    return count


if __name__ == "__main__":
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python program.py <filename>")
        sys.exit(1)

    # Read the range strings from the file
    filename = sys.argv[1]
    with open(filename) as f:
        range_strs = f.read().strip().split("\n")

    # Count the number of pairs where one range fully contains the other
    count1 = 0
    for range_str in range_strs:
        try:
            count1 += count_fully_contained_pairs(range_str.split(","))
        except ValueError:
            # Ignore invalid range strings
            pass

    # Count the number of pairs that overlap at all
    count2 = 0
    for range_str in range_strs:
        try:
            count2 += count_overlapping_pairs(range_str.split(","))
        except ValueError:
            # Ignore invalid range strings
            pass

    print("Number of pairs where one range fully contains the other:", count1)
    print("Number of pairs that overlap at all:", count2)
