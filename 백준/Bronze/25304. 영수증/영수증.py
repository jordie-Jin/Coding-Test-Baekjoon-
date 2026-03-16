x = int(input())
n = int(input())

sol = 0

for i in range(n):
    a, b = map(int, input().split())
    sol += a * b

if x == sol:
    print('Yes')
else:
    print('No')
