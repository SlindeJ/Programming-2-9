import random

pnum = int(input())
cnum = random.randrange(1, 21)
if pnum == cnum:
  print("You Won!")
else:
  print("Better luck next time.")
