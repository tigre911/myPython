from builtins import range

url = 'https://www.acmicpc.net/problem/10819'

# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
#
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

from itertools import permutations

n = int(input())
input_list = permutations(list(map(int, input().split()))) # 받은 배열을 순열로 만들어준다.

result = 0 #결과값을 저장할 변수

for i in input_list:
    print(i) # 순열을 출력해 본다.

for a in input_list:
    sum = 0     #원소의 차를 저장할 변수
    for i in range(n-1):
        sum += abs(a[i] - a[i+1]) #abs() 절대값을 반환해주는 함수 , 각원소의 차의 절대값
    result = max(result, sum) #각 순열의 sum 에 저장된 값과 비교해서 더큰값을 결과값으로 선정

print(result)


# a = list(map(int, input().split()))
# a.sort()
# print(a)
# result = 0
# for i in range(2,n+1):
#     print(f'a[i-2] : {a[i - 2]}')
#     print(f'a[i-1] : {a[i - 1]}')
#
#     A = a[i-2] - a[i-1]
#     print(A)
#     print(abs(A))
#     result += abs(A)
#
# print(result)
#
# 20 1 15 4 10 8