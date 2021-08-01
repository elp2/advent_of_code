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
