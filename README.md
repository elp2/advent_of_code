# advent_of_code_2016

Solutions in 2021.

## Day 1.
Trying out complex() for rotations. Ended up with a bunch of int() and abs() casts.

## Day 2.
Pretty simple.

## Day 14.
Screwed up initially by not generating all triples, because I was only iterating over the range valid for fives.
Pre-calculating FTW since the second round made us do a bunch of hashes.
len(set({comprehension to get indexes 1,2,3})) == 1 is easier to write than a[0] == a[1] and a[1] == a[2].

## Day 15.
Brute force fallback was more than fast enough when LCM method didn't work properly.

## Day 16.
Simple with one miss where I didn't reverse the "b" string initially.
Didn't need any optimization for Part 2.

## Day 17.
Easy once I fixed a bug in Part 2 where I wasn't ending solutions which reached the goal.

## Day 18.
Easy. Didn't even need to optimize for part 2 by caching.

## Day 19.
Did a linked list for first part. My computer couldn't handle the full number of elves so I had to optimize the first round. I couldn't scale this to part 2 so had to come up with a crossing off approach.

# Day 21.
Finally spent some time with np and it made things way easier. For Part 2 I started doing some complicated reversing logic, realized it was a dead end because some things are un-reversable, and then just did the simple brute force check. 

# Day 22.
First part should have been easy if I had remembered that combinations does not expose both orderings a, b and b, a! Part 2 was pretty easy when I broke down the steps.

# Day 23.
Another assembly lang optimization with the same tricks as last time.

# Day 24.
Everything came together here really smoothly after a small problem forgetting about walls.

# Day 25.
Pretty easy - add the new operation, iterate against an expected list and found it quickly.
