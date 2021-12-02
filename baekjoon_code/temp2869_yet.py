a, b, v = map(int, input().split())

for i in range(v+1):
    if v <= i*(a - b) + a :
        print(i+1)
        break