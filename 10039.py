num_arr = []

for i in range(5):
    num = int(input())
    if num < 40:
        num = 40

    num_arr.append(num)

print(int(sum(num_arr) / len(num_arr)))
