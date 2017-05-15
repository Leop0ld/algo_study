clue = input()
n, x = clue.split(' ')

input_num_list = input()
num_list = input_num_list.split(' ')
result = []

for num in num_list:
    if int(num) < int(x):
        result.append(num)

print(' '.join(result))
