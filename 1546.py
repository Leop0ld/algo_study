user_input = input()
input_arr = input().split(' ')
input_arr = list(map(int, input_arr))
result_arr = []

max_num = max(input_arr)

for score in input_arr:
    result_arr.append(score / max_num * 100.0)

average = sum(result_arr) / len(result_arr)

print(average)
