inps = []

inp = int(input())

for i in range(inp):
    inps.append(int(input()))

for i in inps:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
