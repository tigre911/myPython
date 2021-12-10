n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a = a.sort(reverse=False)
# b = b.sort()
print(a, b)
a = sorted(a)
b = sorted(b, reverse=True)
print(a, b)
def s(n):
    result = 0
    for i in range(n):
        result += (a[i]) * (b[i])
    print(result)

s(n)