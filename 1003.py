def fibonacci(n):
    if n == 0:
        print('0', end=' ')
        return 0
    elif n == 1:
        print('1', end=' ')
        return 1
    else:
        if not n == 1:
            return fibonacci(int(n) - 1) + fibonacci(int(n) - 2)
        else:
            return fibonacci(int(n) - 1)


loop_num = int(input())

for i in range(0, loop_num):
    fibonacci(i)
