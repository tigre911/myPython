#이진 탐색 소스코드 구현(반복문)
def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid
        # 중간값이 타겟값과 같아서 찾은 경우 중간값의 인덱스 반환
        elif array[mid] > target:
            end = mid - 1
        # 중간값이 타겟값보다 크다면 왼쪽 값 확인
        else:
            start = mid + 1
        # 중간값이 타겟값보다 작다면 오른쪽 값 확인
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binarySearch(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)