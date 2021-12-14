n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
a = sorted(a)
for i in range(n):
    result += max(a) * min(b)
    # a.pop(a.index(max(a)))
    # b.pop(b.index(min(b)))
    a.remove((max(a)))
    b.remove((min(b)))
print(result)