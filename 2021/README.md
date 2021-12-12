# Day 1

Simple, straightforward.

# Day 2

Lost time on part 1 when I flipped the down/up effect on depth. Otherwise simple.

# Day 3

Pretty simple, with proper, non buggy list comprehension.

# Day 4

Worked better when I broke out the solving / scoring into a separate function.

# Day 5

The parsing took a bit longer, and the delta took a bit longer than needed. But overall it was quickly adaptable to the second question.

# Day 6

Had some minor problems understanding the 6/8 new fish in the beginning. Samples kept me on track. I had a feeling that the array method would be too slow! :) I overcomplicated the part 2 with a separate babies variable, and forgot to account for multiple not just one fish at each gestatation stage.

# Day 7

Wow. This is what happens when you try to program while watching Curb Your Enthusiasm. Not recommended.

# Day 8

Part 2 is the hardest problem so far IMHO. Everything else has been way easier. What cracked it for me was using the relationships between each digit's appearance and what segments are lit.
The weird thing about my solution is that it can sometimes find ambiguous solutions, so I need an additional "check mapping" step. If I knew I was going to have to build that, I just should have just generated all the random mappings with the easy to know numbers fixed, rather than doing the digit subtraction math.

# Day 9

Straightforward. I created an "arounds_inside" function in the template since it would have been useful for this and Day 11.

# Day 10

Generally happy with this one, although I made some dumb mistakes keeping my various mappings straight.

# Day 11

Breaking down into sub functions inside the solve loop made things easier. Made an otherwise dumb mistake around >= 9 rather than correct >= 10.

# Day 12

I did a gross path brute forcing which ran super fast anyway.

Mistakes:
* Forgetting that we could go from/to things when a path was listed
* Going back to start (inf loop)
* Both questions I wasted time chasing a bug which was really me using the wrong pairing of sample / expected values
* Reading part 2 too speedily and assuming we could go to small caves 2x - I was so close to the original solution it shoudln't have taken me 11 minutes.
