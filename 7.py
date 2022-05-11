import sys

filename = 'test' if len(sys.argv) < 2 else sys.argv[1]
width = 20000
height = 100000
def inBounds(x1, y1, x2, y2, x3, y3):
    return x1 < x3 and x1 > x2 and y1 < y3 and y1 > y2

with open(filename) as f:
    l = f.read().splitlines()

notfreeSpace = 0

for i in range(height):
    if i % 100 == 0:
        print(i)
    for j in range(width):

        for k in l:
            x, y, w, h = [int(x) for x in k.split()]
            if inBounds(j, i, x, y, x + w, y + h):
                notfreeSpace += 1
                break

print(height * width - notfreeSpace)
