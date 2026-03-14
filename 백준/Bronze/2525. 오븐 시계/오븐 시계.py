h, m = map(int, input().split())
add = int(input())
m += add
h += m//60
m %= 60
h %= 24
print(h, m)