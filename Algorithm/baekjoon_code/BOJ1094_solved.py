url = "https://www.acmicpc.net/problem/1094"

sticks = [64,32,16,8,4,2,1]
counts = 0
x = int(input())
for i in sticks:
    counts += x // i
    x %= i

print(counts)