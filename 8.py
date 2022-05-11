import sys

def encode(key, charset, msg):
    encoded = ""
    longKey = key * (len(msg) // len(key))
    longKey = longKey + key[:len(msg) % len(key)]
    for i in range(len(msg)):
        if msg[i] in charset:
            encoded += charset[(charset.index(longKey[i]) + 1 + charset.index(msg[i])) % len(charset)]
        else:
            encoded += msg[i]

    return encoded


def decode(key, charset, msg):
    decoded = ''
    longKey = key * (len(msg) // len(key))
    longKey = longKey + key[:len(msg) % len(key)]
    for i in range(len(msg)):
        if msg[i] in charset:
            decoded += (charset[(charset.index(msg[i]) - (charset.index(longKey[i]) + 1)) % len(charset)])
        else:
            decoded += msg[i]

    return decoded

filename = '8.in' if len(sys.argv) < 2 else sys.argv[1]
with open(filename) as f:
    l = f.read().splitlines()

charset = [x for x in l[0]]
key = l[1]
msg = l[2]
decoded = decode(key, charset, msg)
print(decoded)
