#이진 탐색 소스코드 구현(재귀함수)
def binary_search(array, target, start, end):
    if start > end :
        return None

    mid = (start + end)//2

    if array[mid] == target:
        return mid
    # 찾고자 하는 값이 mid와 같다면 mid 를 return(출력)
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1 , end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)