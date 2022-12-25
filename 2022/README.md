# 2022 Overview

I'm also trying these early questions in GPT Chat (after I finish them honestly myself!)

# Day 1
GPT Chat was very quick to write this.

# Day 2
I could not get GPT Chat to properly handle the rules grid. Maybe it would have been easier to convince it to add the chosen shape score rather than putting it in the state grid. It seemed pretty far away for Part 2 and Day 3 was about to start so I stopped trying to get it to work.

# Day 3
GPT worked great for part 1, once I told it to read from standard input. This actually even finished faster than my solution.
Part 2 seemed to be confused about the splitting lines up rule, but was grouping the lines properly.

# Day 4
The easiest one this year IMHO. GPT Chat had almost no problem solving it as well.

# Day 5
Definitely trickier than yesterday, mostly on the parsing part. Once I had the arrays it was pretty simple. Parsing could have been pretty fast if I'd just gone column by column based on the char x, ys, rather than using the column identifiers.

# Day 6
First part was easy. Then I must have made a mistake copying the sample, and I had the right solution but it wouldn't match the expected sample output.

# Day 7
The pre-parsing of commands was a waste - I just parsed them so I could unpack them later. Same with saving the individual files and sizes, although you never know on Part 2!

# Day 8
That was just much harder than it should have been. At least my parse through neighbors code was pretty reusable.

# Day 9
This took way too long for Part 2. In the end, I was being way too tricky and I was missing some diagonal casees.

# Day 10
Intcode v2? My Part 2 had some bug printing the first line but it was legible enough to get the answer.

# Day 11
I really need to look up how Python class types work.

# Day 12
I solved P1 pretty fast, and I was on a good track for P2 I think, but I got stuck on the conditional for going down. I needed to it to be just paths that involved jumps of 0/1, but I had the wrong conditions.

# Day 13
I over-estimated the difficulty and didn't tackle this for a few days. Part 2 flowed pretty easily but I always forget how to pass the comparator function to the sorted, so I created "elpsort"

# Day 14
Pretty straightforward transforming the rules.

# Day 15
For some reason I had trouble getting the diagonal stepping to work properly as I walked it along the edge...

# Day 16
This one really hurt my brain for some reason and I'm not sure why. Part 1 was pretty straightforward, but Part 2 I just made the algo for a given set as fast as possible, then ran it in parallel on my M2 so it finished in about an hour. Should investigate bitmasks since it might have made the caching, etc faster.

# Day 17
Part 1 was pretty simple. Part 2 ended up being easier than I was expecting - just getting the repeating rock indexes, pieces. There was a nice trick that the example repeated in the first round, but the actual only repeated in the second occurance.

# Day 18
I found this super straightforward. My algo easily generalized to Part 2.

# Day 19
I think I let this one psyche me out. Ultimately I thought more about it and realized the goal was to get to "escape velocity" where you could buy a geode miner every turn. So all states needed to move us towards having enough ore/obs to build that.

# Day 20
My cursed problem. Part 1 was one of those where I couldn't imagine why it was so hard. I chose a linked list, which made accessing them later to move easier, but I made stupid mistakes trying to collapse +/- moves to the same function. Splitting them out made this work first try (once I realized I wasn't calling the new function :)). Part 2 flew based on my previous banging head investigation.

# Day 21
Part 1 was straightforward. Part 2 I spent waaay too much time trying to apply the chain rule while drunk after dinner. I knew it was going to be linear and could calculate the slope. I knew I needed to calculate the slope, but I kept screwing it up and had to brute force the ending. Beer/beach may have been involved.

# Day 22
Probably the most fun puzzle of the year. The first part was a nice straightforward coding challenge, and the second part required (at least me) to cut out a cube to see how moving between zones would affect the facing.

# Day 23
Pretty straightforward, Part 2 flowed if Part 1 was efficient enough.

# Day 24
Fun. I missed some silly rules like it could stay still. I found the boundary conditions much harder until I just removed all the #'s and adjusted the height.

# Day 25
Complete! I wasted a lot of time converting them into ints, and then back, when actually just adding them was not that hard.