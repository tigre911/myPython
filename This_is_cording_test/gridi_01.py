money = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_list = [500, 100, 50, 10]

for coin in coin_list:
    count += money // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    money %= coin # %= 할당 연산자 - 연산자의 왼쪽 값에서 오른쪽 값을 나눈 값의 나머지를 왼쪽에 할당한다.
    print(f'coin:{coin}')
    print(f'count : {count}')
    print(f'money : {money}')
print(count)