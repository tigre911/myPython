url = 'https://www.acmicpc.net/problem/1149';
#문제를 못알아 먹겠다 ㅠㅠ
import sys
input = sys.stdin.readline

n= int(input())
RGB = []

for i in range(n):
    RGB.append(list(map(int, input().split())))

print(RGB)

for i in range(n):
    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]
print(min(RGB[n - 1][0], RGB[n - 1][1], RGB[n - 1][2]))