lines = []
while (inp := input()):
    lines.append(inp)
dd = dict()
for i in range(65, 91):
    dd[chr(i)] = 0


equalFlag = False
i = 0

def returnSourceData(source):
    if source.isalpha():
        return dd[source]
    else:
        return int(source)

while True:
    instr = lines[i].split()
    op = instr[0]
    
    if op == "ADD":
        target, source = instr[1:]
        dd[target] += returnSourceData(source)

    elif op == "CGE":
        s1, s2 = instr[1:]
        equalFlag = returnSourceData(s1) >= returnSourceData(s2)
    
    elif op == "CEQ":
        s1, s2 = instr[1:]
        equalFlag = returnSourceData(s1) == returnSourceData(s2)

    elif op == "OUT":
        print(returnSourceData(instr[1]))

    elif op == "MOD":
        target, source = instr[1:]
        dd[target] %= returnSourceData(source)

    elif op == "DIV":
        target, source = instr[1:]
        dd[target] //= returnSourceData(source)

    elif op == "MOV":
        target, source = instr[1:]
        dd[target] = returnSourceData(source)

    elif op == "END":
        break

    elif op == "JMP":
        i += returnSourceData(instr[1])
        continue

    elif op == "JIF":
        if equalFlag:
            i += returnSourceData(instr[1])
            continue

    i += 1
