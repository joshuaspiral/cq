import hashlib
with open('5.in') as f:
    blockchain = f.read().splitlines()

def sha256(strn):
    return hashlib.sha256(strn.encode()).hexdigest()

for i in range(7, len(blockchain)):
    split = blockchain[i].split('|')
    minedNumber = 0

    if i > 0:
        split[2] = blockchain[i - 1].split('|')[-1]
    while True:
        split[1] = str(minedNumber)
        strn = '|'.join(split[:-1])
        hashed = sha256(strn)
        if hashed[:6] == "000000":
            break
        minedNumber += 1

    split[-1] = hashed
    blockchain[i] = '|'.join(split)
    print(blockchain[i])
