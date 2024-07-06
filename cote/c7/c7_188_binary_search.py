# 이진탐색 : 배열 내부의 데이터가 정렬되어 있다면, 빠르게 데이터를 찾을 수 있는 알고리즘
# 탐색 범위를 절반씩 좁혀가며 데이터 탐색
# 이진탐색의 변수 3가지 : 시작점, 끝점, 중간점
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
# 시간복잡도 O(NlogN)
# 자료구조의 범위가 매우 크다면, 이진 탐색 알고리즘을 의심해볼 수 있다.
# 입력데이터가 많은 경우, input()함수 사용시 동작속도가 느리므로 아래를 사용할 수 있다.
# import sys
# 하나의 문자열 데이터 입력받기
# input_data = sys.stdin.readline().rstrip()        # rstrip() : readline으로 생성된 줄바꿈기호(엔터)를 제거

# 입력받은 문자열 그대로 출력
# print(input_data)



# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 함수 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)