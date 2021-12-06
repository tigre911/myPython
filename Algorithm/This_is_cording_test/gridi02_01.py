# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# n : 배열의 크기, m : 숫자가 더해지는 횟수 , k : 몇번 더할지
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
max_num = data[n - 1] # 가장 큰 수
second_max_num = data[n - 2] # 두 번째로 큰 수

max_count = (m // (k + 1)) * k    #큰수를 더해주는 횟수 m번 더해주는데 k번만 더할수 있으니 m을k로 나눈 몫에 k를 곱해줌
max_count += m % (k + 1)    #두번째 큰 수를 더해주는 횟수 m을 k로 나눈 나머지
print(max_count)
# print(second_count)
# result = (max_count * max_num) + (second_count * second_max_num)

print(result)
print(f'fff : {6+6+5+6+6+5+6+6}')