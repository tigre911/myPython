url = 'https://www.acmicpc.net/problem/4673'

def fun(n):
    while True:
        n += n + (n//1000) + (n//100) + (n//10)
        if  n < 10000:
            break
        print(n)
fun(1)