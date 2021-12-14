k, n, m = map(int, input().split())

money = (n * k) - m

if money >= 0 :
    print(money)
else:
    print(0)