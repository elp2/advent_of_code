# Advent of Code Solutions 2024

## Summary
Overall, this year seemed relatively easy and 2D puzzle heavy. 
My favorites were: 24, 21, 17, 15, 14.

## Day 25
Straightforward to the end! I feel overly smart about my lock flipping strategy lol.

## Day 24
I liked this one. I did a combination of manual finding for the first few, and then built something that swapped all the potentially troublesome pairs until math started working. I wonder how much harder it would have been if they were not swapped adjacent/in the same path to the end? Also, if they didn't follow a true adder but had some decoy nodes in there.

## Day 23
Part 2 flowed from part 1 to just keep merging the 3 groups until you couldn't merge any more.

## Day 22
A breeze after 21. Part 2 really flowed naturally from Part 1, more of a part 1.5.

## Day 21
I think this was the hardest puzzle of the bunch. The indirections made the reasoning harder for me.

## Day 20
I actually ended up solving this one last. My intuition of just going everywhere manhattan distance away was right, but I forgot my best map had starting walls in it for some reason.

## Day 19
This didn't seem like a Day 19 from previous years in terms of difficulty? Most of my time here was spent on a stupid error in my cache which always returned True :).

## Day 18
Back to 2D land I guess. I thought that they were going to fall in one by one and we'd have to navigate around them, which would have been interesting. But it ultimately was just "Run Part 1 in a loop".

## Day 17
There were a lot of rules to parse. Once I started exploring the space and looking at the program, it became clear that we could just keep track of the prefixes that worked and Part 2 fell quickly. A pretty fun question and a nice break from 2D land.

## Day 16
As of right now it seems like I'm finding pretty much everything, but I must be missing one path.

## Day 15
Overall a fun one. There seem to be a lot of problems about things moving around this year.

## Day 14
My favorite one of the year so far. When I saw the prime number sizes, I thought we'd run to 10 million seconds or something, but this was a nice surprise.

## Day 13
The edge conditions for Part 1 were tricky for some reason. Maybe I was underestimating it. Part 2 was simple algebra.

## Day 12
The trick to Part 2 was to draw out the boxes and thought of what made a convex/concave corner.

## Day 11
I way overcomplicated Part 1 with a Linked List assuming the positions would matter in the second round. Then I had to rewrite Part 2 to use Counters. I should be using Counters over defaultdicts any time there are integer values!

## Day 10
The problem was a bit hard to parse, I overcomplicated it in the beginning. Part 2 was actually more natural in some ways than Part 1, since you could use a deque the whole way, rather than needing to dedupe the next set of items.

## Day 9
Not that hard, but in my defense I had some eggnog!

## Day 8
Python combinations made quick work of this one. Other than the antennas now being automatic antinodes of themselves on Part 2 the Part 1 solution was mostly good enough.

## Day 7
The easiest one this cycle by far.

## Day 6
The trickiest part was that the obstacles could be placed diagonally to each other, which resulted in a non 90 degree turn. 

## Day 5
Part 1 was pretty straightforward. Initially separating out the validation into a separate function would have made Part 2 faster.

## Day 4
Luckily we are not handling corruped memory IntCode (AOC 2019) style... yet.
Part 1 went pretty quickly, and I would have had Part 2 momentarily afterwards if I hadn't put down -1, -1 / 1, 1 as my delta... that was just comparing the same lines!!!

## Day 3
It's funny because I played around with the parse library this morning since I thought it could help avoid regex, but this one was so much easier to solve using findall!

## Day 2
For some reason this was way harder than it should have been.
I couldn't run the debugger, which made the problem worse. Had to rewrite in the morning to redeem myself and test my new tempalte changes.

## Day 1
Pretty easy, just easing back into my template.