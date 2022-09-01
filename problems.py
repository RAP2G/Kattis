inp = int(input())

if inp < 100:
    print(99)
else:
    a = inp % 100
    if a < 49:
        print(inp-a-1)
    else:
        print(inp+(99-a))
