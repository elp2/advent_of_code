# advent_of_code_2016

Solutions in 2021.

## Day 1
Trying out complex() for rotations. Ended up with a bunch of int() and abs() casts.

## Day 2
Pretty simple.

## Day 3
Easy. The separate directory seemed to be more trouble than it was worth so I stopped doing that.

## Day 4
Pretty easy.

## Day 5
Fun, not too hard.

## Day 6
I feel that itemgetter isn't as straightforward than a comparing function.

## Day 7
re.split is a powerful tool!

## Day 8
Pretty straightforward. Added some nicer constants for printing things out in the future.

## Day 9
OK with the class I created, although fancier parsing practice would probably be useful for problems like this.

## Day 10
I had some copy/paste errors from the low/high and handling robots and outputs separately - probably easiest to just all treat them as buckets and differentiate based on names.

## Day 12
Love these intcode puzzles! Optimizing was pretty easy.

## Day 13
A simple deque and BFS solved quickly.

## Day 14
Screwed up initially by not generating all triples, because I was only iterating over the range valid for fives.
Pre-calculating FTW since the second round made us do a bunch of hashes.
len(set({comprehension to get indexes 1,2,3})) == 1 is easier to write than a[0] == a[1] and a[1] == a[2].

## Day 15
Brute force fallback was more than fast enough when LCM method didn't work properly.

## Day 16
Simple with one miss where I didn't reverse the "b" string initially.
Didn't need any optimization for Part 2.

## Day 17
Easy once I fixed a bug in Part 2 where I wasn't ending solutions which reached the goal.

## Day 18
Easy. Didn't even need to optimize for part 2 by caching.

## Day 19
Did a linked list for first part. My computer couldn't handle the full number of elves so I had to optimize the first round. I couldn't scale this to part 2 so had to come up with a crossing off approach.

# Day 20
This was way harder for me than it should have been for some reason. Things that made it easier in the end: sort by start and then keep folding into the sorted list.

# Day 21
Finally spent some time with np and it made things way easier. For Part 2 I started doing some complicated reversing logic, realized it was a dead end because some things are un-reversable, and then just did the simple brute force check. 

# Day 22
First part should have been easy if I had remembered that combinations does not expose both orderings a, b and b, a! Part 2 was pretty easy when I broke down the steps.

# Day 23
Another assembly lang optimization with the same tricks as last time.

# Day 24
Everything came together here really smoothly after a small problem forgetting about walls.

# Day 25
Pretty easy - add the new operation, iterate against an expected list and found it quickly.
