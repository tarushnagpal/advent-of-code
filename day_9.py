# part 2, remove the * 100 for part 1

import time
import math
import collections
import re
current_milli_time = lambda: int(round(time.time() * 1000))
start = current_milli_time()

# Input
players = 431
lastpoint = 70950

circle = collections.deque()

circle.append(0)

elf = 0
maxscore = 0
scores = collections.defaultdict(int)
player = 1
for x in range(1, lastpoint+1):
  if (x % 23) == 0:
    circle.rotate(-7)
    scores[player] += (x + circle.pop())
    if scores[player] > maxscore:
      maxscore = scores[player]
      elf = player
  else:
    circle.rotate(2)
    circle.append(x)
  player += 1
  if player > players:
    player = 1

print("Part 1: ", maxscore)

# print((current_milli_time() - start) / 1000.0)

#Part 2 

players = 431
lastpoint = 70950*100

circle = collections.deque()

circle.append(0)

elf = 0
maxscore = 0
scores = collections.defaultdict(int)
player = 1
for x in range(1, lastpoint+1):
  if (x % 23) == 0:
    circle.rotate(-7)
    scores[player] += (x + circle.pop())
    if scores[player] > maxscore:
      maxscore = scores[player]
      elf = player
  else:
    circle.rotate(2)
    circle.append(x)
  player += 1
  if player > players:
    player = 1

print("Part 2: ", maxscore)

# print((current_milli_time() - start) / 1000.0)