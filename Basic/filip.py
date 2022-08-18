inp = input()

one, two = inp.split(" ")
one = int(one[::-1])
two = int(two[::-1])

if two > one:
    print(two)
else:
    print(one)
