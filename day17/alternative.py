import sys
from collections import defaultdict

containers = list(map(int, open('input')))

c = 0
m = sys.maxsize
variants = defaultdict(int)
for v in range(1 << len(containers)):
   t = v
   s = 0
   n = 0
   for j in containers:
      if t & 1 == 1:
         s += j
         n += 1
      t = t >> 1

   if s == 150:
      c += 1
      variants[n] += 1
      if m > n:
         m = n

print('Part1: ', c)
print('Part2: ', variants[m])
