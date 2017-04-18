kilogram = int(input())

five = kilogram // 5
three = 0

kilogram %= 5

while five >= 0:
    if kilogram % 3 == 0:
        three = kilogram // 3
        kilogram %= 3
        break

    five -= 1
    kilogram += 5

print(five + three)
