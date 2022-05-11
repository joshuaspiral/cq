import math
with open('3.in') as f:
    l = [[int(i) for i in x.split()] for x in f.read().splitlines()]

totalDist = 0
for i in range(len(l)-1):
    x1, y1, z1, = l[i]
    x2, y2, z2, = l[i+1]
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    totalDist+=math.trunc(dist)

print(totalDist)



