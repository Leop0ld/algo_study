num = int(input()) + 1

for i in range(1, num):
    for j in range(num - i - 1):
        print(' ', end='')

    for k in range(i):
        print('*', end='')

    print('')
