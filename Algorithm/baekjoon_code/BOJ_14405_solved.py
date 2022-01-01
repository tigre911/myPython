#1

import re

text = input()

p = re.compile('(pi|ka|chu)+')

if p.fullmatch(text): print('YES')
else: print('NO')

#2

S = input()

# 조건을 만족하는 경우 계속 반복문을 돌기 위해 while문 사용
while True:
    # pi라는 문자가 있는 경우 pi라는 문자를 공백으로 대체
    # find함수를 이용하여 문자를 찾게되면 존재하는 경우 최소 인덱스 값인 0 이상을 반환할 것이다.
    # 문자가 존재하지 않는 경우 -1을 반환하기 때문에 이러한 성질을 이용하여 0보다 크거나 같다는 조건을 주었다.
    if S.find('pi') >= 0:
        S = S.replace('pi', ' ')
        continue
    elif S.find('ka') >= 0:
        S = S.replace('ka', ' ')
        continue
    elif S.find('chu') >= 0:
        S = S.replace('chu', ' ')
        continue

    # 위의 조건에서 문자를 제외하고 공백을 주었다
    # 그렇기 때문에 공백을 제거하고 붙이기 위해 strip함수를 사용
    # 결과적으로 문자열의 길이가 0이면 발음가능 아닐경우 발음 불가능
    if len(S.strip()) == 0:
        print('YES')
        break
    else:
        print('NO')
        break