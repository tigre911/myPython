url = 'https://programmers.co.kr/learn/courses/30/lessons/42839'

from itertools import permutations

def solution(n):
    prime = set()
    # 1. 모든 숫자 조합을 만든다
    for i in range(len(n)):
        print("list(n) : " , list(n)) # n의 string을 하나씩 자른다.

        print("list(permutations(list(n), i + 1)) : " , list(permutations(list(n), i + 1)))
        # list(n)으로 부터 i+1개짜리 순열을 만들어 tuple로 반환한다
        # 순열이란 n개의 원소를 사용해서 순서를 정하여 r개의 배열로 나타내는 것을 말한다.
        # 순열은 순서가 있기 때문에 원소의 종류가 같아도 순서가 다르면 다른배열이 된다.

        print(list(map("".join, permutations(list(n), i + 1))))
        # map이란 반복가능한 객체에 각각 함수를 적용하고 싶을 때 사용하는 함수

        print(list(map(int, map("".join, permutations(list(n), i + 1)))))
        # int로 map함수 다시 사용하여 캐스팅

        prime |= set(map(int, map("".join, permutations(list(n), i + 1))))
        # 합집합들을 대입
        print(f'prime : {prime}')

    # 2. 소수가 아닌 수를 제외한다.
    prime -= set(range(0, 2))
    for i in range(2, int(max(prime) ** 0.5) + 1):
        prime -= set(range(i * 2, max(prime) + 1, i))
    return len(prime)


print(solution("17"))