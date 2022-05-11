winningNumbers = "12 48 30 95 15 55 97"
winningNumbers = [int(x) for x in winningNumbers.split()]
with open('2.in') as f:
    l = [[int(i) for i in x.split()] for x in f.read().splitlines()]

def getPrize(num):
    return int("1" + ("0" * (num - 3)))

total = 0
for i in l:
    rightNums = 0 
    for j in i:
        if j in winningNumbers:
            print(i)
            rightNums += 1;
    if rightNums >= 3:
        total += getPrize(rightNums)

print(total)
