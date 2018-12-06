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
Honestly you can just use sum() here but like can we sometimes not leave things completely to python?

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

## Day 3
#### Part 1
Okay so, I like this question. Imagine a plot of land, where each person claims a part of the land for themselves. But, theres a chance that multiple people own the same part of land! In the first part we just need to find out how much of the land is owned by more than one person. Ez. 

Think of it this way, initialize a matrix with just \*'s. Cool? Cool. 
Now we decipher our input to get all the land that the person has taken for themselves, using

```
# Here x is each line in our input file
id = x[ :x.index('@')-1 ]
pos_x = int(x[ x.index('@') + 1:x.index(':')].split(',')[0])
pos_y = int(x[ x.index('@') + 1:x.index(':')].split(',')[1])
len_x = int( x[x.index(':')+1:].split('x')[0] )
len_y = int( x[x.index(':')+1:].split('x')[1] )
```

Now we have a small rectangle in out matrix starting from ```(pos_x,pos_y)``` with a height of ```len_y``` and a breadth of ```len_x```, this small rectangle is the part of the land that belongs to ```id```. 

Now to finally solve the problem at hand. Consider there to be 3 states
1. State 1: matrix\[i\]\[j\] is a '\*' that means unclaimed land
2. State 2: matrix\[i\]\[j\] is a '\#' that means land claimed by 1 user
3. State 3: matrix\[i\]\[j\] is a 'X' that means land claimed by more than 1 user

For all values in this rectangle, 
If we see a '\*' it means that this is unclaimed land and we change this to a '\#' claimed by 1 user, i.e. us
If we see a '\#' it means that this has already been claimed by a user and we change it to a 'X' and that's it.

Now all we do is count the number of X's and that's our answer!

#### Part 2
Okay I'll give you a visualization of our matrix:
!["Day 3 Matrix"](https://raw.githubusercontent.com/CallMeTarush/advent-of-code/master/files/day_3_matrix_visual.png "Day 3 Matrix")

In the above scheme, 
1. The yellows are the \*'s
2. Light pinks are the \#'s
3. Reds are the X's
4. Green is our solution for part 2!

How to arrive at the solution for part 2?
Ez.
You already have the answer with you, all we need to do in our code is now calculate the total area for each portion of land,

```
total_len = len_x*len_y
```

Now that we have our area we just check if each id in all of its area has any X's. If it doesn't then yay! That's your solution.

```
for i in range(len_x):
  for j in range(len_y):
    if(fabric_matrix[pos_x+i][pos_y+j] == 'X' ):
      check_unique = False
      break
```

## Day 4 
Alright, Day 4 is a little trickier than what we have encoutered uptill now,

We are given an input as :
```
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
```

#### Part 1
And we need to find out which guard is asleep the most at any minute and well find that minute
Cool so lets divide Part 1 into two

##### Part 1 - Part1(xD) Finding the guard who sleeps the most
  First we need to sort the inputs according to the date and time (THANK YOU PYTHON)
  ``` inputs.sort(key=lambda date: datetime.strptime( date[ date.index('[')+1:date.index(']') ] , "%Y-%m-%d %H:%M"))```
  pretty chill, finds the date and sorts with the key as the date.
  
  Now I've made 3 dictionary's here, easier for us to use for part 2 as well.
  The first,
  
  ```
  guard[id] => total_minutes_he_slept
  guards_start_times[guard_id] => [all_times_he_has_started_to_sleep]
  guards_end_times[guard_id] => [all_times_he_has_woken_up]
  ```
##### Part 1 - Part2 Finding which minute the guard sleeps the most
  Now, each index in the list of the two arrays ```[all_times_he_has_started_to_sleep]``` and ```[all_times_he_has_woken_up]``` have matching indeces, the start_time and the coressponding end_time. Now all we do is make a dictionary of all the minutes which point to the number of times the guard has been slept for this specific time. And the maximum value for a (key,value) in this dictionary is the minute!

#### Part 2
  In this part we need to find which guard has been asleep the most for a any minute in all the time he has been asleep, and find the max from all the guards. 
  
  So what we did for part 1 - part 2 for just the best guard we need to do this for every guard. So find start_time, find end_time and apply our ```perdelta``` function for each time interval, find the minute with the most occurences and record that for the guard. Then just find the guard with the most slept through minute. And we have our answer!
  
## Day 5
#### Part 1
Alright, Pretty easy question. We have a string of the form aAbBcC, if any two consecutive letters are the same letter but just have a change in their Case then we delete them from the list. I used the ord() function for this and just had a:

```
if( abs(ord(items[i]) - ord(items[i+1])) == 32 ):
del(items[i])
del(items[i]) #delete 'i' again because the i+1<sup>th</sup> item is now on the i<sup>th</sup> position 
change = True #Keeping track of a change if there is no change once going through the string then we break from our loop
```

Now the length of the list items is the answer for part 1

#### Part 2
Now we need to just do part 1 and keep a track of the length of the list of items after removing 'a','b','c' uptil 'z'

So we just add 
```
for i in range(len(new_items)):
        try:        
            if( (ord(new_items[i])==worst_ord) or (ord(new_items[i])+32==worst_ord) ):
                pass
            else:
                items_to_check.append(new_items[i])
```

```items_to_check``` now contains all the items which do not contain the current letter and then we perform part 1 and store the length of the string

And finally the answer for part 2 is the maximum length we receive after removing specific alphabets from the string.

## Day 6
_Visualizing using p5.js gonna upload after my classes_


  


