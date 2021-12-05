n, m, k = map(int, input().split())
# n = 배열크기 / m = 주어진 수를 m번 더함 / k = 연속해서 k번 초과하여 더해질 수 없음
input_list = list(map(int, input().split()))

input_list.sort()

print(input_list)

max_num = input_list[n-1]
second_max_num = input_list[n-2]

print(max_num)
print(second_max_num)

while True:
    if m + k >= n:
        print(max_num * (k-1)) + (second_max_num * (m - k))
        break
    