# 첫째 줄에 (A+B)%C,
# 둘째 줄에 (A%C + B%C)%C,
# 셋째 줄에 (A×B)%C,
# 넷째 줄에 (A%C × B%C)%C를 출력한다.

user_input = input()
a, b, c = user_input.split(' ')

a, b, c = int(a), int(b), int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print(a * b % c)
print((a % c) * (b % c) % c)
