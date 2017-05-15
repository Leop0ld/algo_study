num = int(input()) + 1

for i in range(1, num):
    for j in range(i - 1):
        print(' ', end='')

    for k in range(num - i):
        print('*', end='')

    print('')
