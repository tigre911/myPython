# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# n : 배열의 크기, m : 숫자가 더해지는 횟수 , k : 몇번 더할지
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
max_num = data[n - 1] # 가장 큰 수
second_max_num = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += max_num
        m -= 1
    if m == 0 :
        break
    result += second_max_num
    m -= 1

print(result)
