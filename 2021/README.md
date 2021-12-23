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

# Day 13

Hoooh boy. Some silly ones here.
Copied and pasted my x code into my y folds code, so I was folding based on y coord. Samples saved me here though TBH.
Forgot that I was looking at more than just the first item, thought I broke something between P1/P2.
Parsing worked pretty much first time which was a win.

# Day 14

Got through Part 1 with a minimal number of typos. Then realized the approach obviously wouldn't work for a giant size. Went and got some eggnog, and then came up with this pairwise version. It could have been simpler in hindsight by not doing the special case for the first item, but it worked out OK.

# Day 15

Yuck. I found this way harder than it needed to be. In the end, this was the trick for me:
* Write a BFS without bugs
Took a while to run, but ended up with the right answers.

# Day 16

I enjoyed this one. It became a lot easier when I realized you never needed to go back, and could just grab out of the array. Then you didn't need to be as careful with the indexes.

# Day 17

I made this one about 100x harder than it needed to be but I had fun.

# Day 18

Ultimately, I'm pretty happy with my solution except I missed the instructions that you needed to keep exploding, until you split. Breaking the explode into before/after arrays was simpler than trying to create after the fact. And easier to verify.

# Day 22

I originally had a different "subtract" method of dividing which I couldn't get to work. This one made it a lot simpler by considering the all the possible boxes resulting from the subtraction and removing the ones which were not valid.
