n = 1260
coin_list = [500, 100, 50, 10]
count = 0 #전역변수 설정

for coin in coin_list:
    print(f'n : {n}')
    count += n // coin
    n %= coin
    print(f'coin : {coin}')
    print(f'count : {count}')
print(count)