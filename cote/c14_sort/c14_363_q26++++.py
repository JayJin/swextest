# Q26. 카드 정렬하기
# https://www.acmicpc.net/problem/1715

# 힙은 기본적으로 최소힙
# 최대 힙으로 사용하려면 heapq.heappush(max_heap, (-item, item)) 와 같이 활용

import heapq

n = int(input())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0

# 힙(heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)       # 가장 작은 원소를 추출
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)



'''
input:
3
10
20
40

output:
100
'''