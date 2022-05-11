import sys

def decode(key, charset, msg):
    decoded = ''
    for i in range(len(msg)):
        if msg[i] in charset: decoded += (charset[(charset.index(msg[i]) - (charset.index(key[i % len(key)]) + 1)) % len(charset)]) 
        else: decoded += msg[i]
    return decoded

filename = '8.in' if len(sys.argv) < 2 else sys.argv[1]

with open(filename) as f:
    l = f.read().splitlines()

charset, key, msg = l
charset = [x for x in charset]

print(decode(key, charset, msg))
