user_input = input()
n1, n2, n3 = user_input.split(' ')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if (n2 <= n1 <= n3) or (n3 <= n1 <= n2):
    print(n1)
elif (n1 <= n2 <= n3) or (n3 <= n2 <= n1):
    print(n2)
elif (n1 <= n3 <= n2) or (n2 <= n3 <= n1):
    print(n3)
