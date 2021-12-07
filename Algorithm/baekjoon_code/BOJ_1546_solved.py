url = 'https://www.acmicpc.net/problem/1546'

n = int(input())
score = list(map(int, input().split()))
#list도 map,split을 사용해 입력받을 수 있다!
m = max(score)

new_score_sum = 0
for i in range(n):
    new_score_sum += (score[i] / m * 100)

print(new_score_sum/n)