num1 = int(input())
num2 = int(input())
num3 = int(input())
result_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]


def calculate(num, arr):
    while num > 0:
        tmp = num % 10
        arr[tmp] += 1
        num //= 10

calculate(num1 * num2 * num3, result_arr)

for i in result_arr:
    print(i)
