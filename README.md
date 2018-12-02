# advent-of-code

What is Advent of Code? [Advent of Code](https://adventofcode.com/2018/about) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. ( Totally not copied from their website ) 

Advent of code in simple readable python! This is not a repo where you can see amazingly optimized well written codes, this is just a repo containing all the solutions for the advent of code 2018 in simple beginner friendly python, If you're someone just starting out with python and are stuck on a question in the AOC, this is the repo for you!

As you will see through this document my markdown skills are still at the lower end of the learning curve, IF you guys see anything you want to change in the code that would make it more efficient (but still keep it beginner friendly) or if you see my markdown being completely weird or unreadable put up a PR!

I'll also explain the crucial parts of the code wherever neccesary and put important snippets in this markdown! 

P.S. If I'm a little late on solutions I'm extremely sorry since I am in India and I have college on at the exact time of the new question coming out :(

Good Luck!

## Day 1
#### Part 1
Pretty straight forward, We need to take the sum of the frequencies and get our answer, Straight up code in:

``` total += i ```

#### Part 2
In this part all we have to do is keep a track of all the frequencies that we have seen till now and if any repeats then Boom! We get our answer

``` viewed.add(freq) ```

## Day 2
#### Part 1
In this question we needed to check if the string contained:
1. A character repeated exactly twice
2. A character repeated exactly thrice

If any of these conditions were true just add 1 do the total characters seen twice or thrice!

```
if(counts[i] == 3 and not check_3):
  check_3 = True
elif(counts[i] == 2 and not check_2):
  check_2 = True
```

#### Part 2
This part was pretty straight forward, we needed to check the number of characters that were different in two strings *at the same indices* And if the number of changes were exactly 1 you, you remove this change and get your answer!

```
for z in range(id_length):
  if( ids[i][z]!=ids[j][z] ):
    num_different += 1
    if(num_different > 1):
      break
```                    

