num = int(input())

answer_list = []
i = 1
j = 2

while i < 1000000000:
    answer_list.append(i)
    i += j
    j += 1

quotient = num // 6
print(quotient + 1)
print(answer_list[:15])
