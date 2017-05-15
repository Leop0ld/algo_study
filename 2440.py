num = int(input()) + 1

for i in range(1, num):
    for k in range(num - i):
        print('*', end='')

    print('')
