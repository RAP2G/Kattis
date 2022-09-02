inp = input().split()
time, price = inp
time = int(time)
price = int(price)
day = 0
time_elapsed = 0
old = 5
new = 60
old_lamps_bought = 1
new_lamps_bought = 1


while old <= new:
    if time_elapsed/1000 > old_lamps_bought:
        old += 5
        old_lamps_bought += 1
    if time_elapsed/8000 > new_lamps_bought:
        old += 60
        old_lamps_bought += 1
    old += (60*time*price)/100000
    new += (11*time*price)/100000
    time_elapsed += time
    day += 1
else:
    print(day)
