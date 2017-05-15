num_list = input()

count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

for num in num_list:
    count_list[int(num)] += 1

count_list[6] += count_list.pop(9)

max_count = max(count_list)

if max_count != count_list[6]:
    print(max_count)
else:
    remain = max_count % 2
    max_count //= 2

    if remain != 0:
        max_count += 1

    print(max_count)
