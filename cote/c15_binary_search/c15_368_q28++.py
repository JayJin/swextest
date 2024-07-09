# Q28. 고정점 찾기
# 고정점(Fixed point) : 수열의 원소 중 값이 인덱스와 동일한 원소

# 이진탐색을 수행할 때에는 '찾고자 하는 값'이 '중간점'과 동일하다고 가정하고 탐색을 수행한다.

def bi_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return bi_search(array, mid + 1, end)
    else:
        return bi_search(array, start, mid-1)


n = int(input())
array = list(map(int, input().split()))

result = bi_search(array, 0, n)     # n → n-1?

if result == None:
    print(-1)
else:
    print(result)



'''
input(1):
5
-15 -6 1 3 7

output(1):
3

input(2):
7
-15 -4 2 8 9 13 15

output(2):
2

input(3):
7
-15 -4 3 8 9 13 15

output(3):
-1
'''