# dijkstra 알고리즘의 개선방식
# 시간복잡도가 O(ElogV)
# 힙(Heap) 자료구조를 사용
# 특정 노드까지의 최단거리에 대한 정보를 힙에 담아서 처리하므로
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

# 우선순위 큐(Priority Queue) : 가장 우선순위가 높은 데이터부터 추출
# 구현시 내부적으로는 최소 힙(Min heap) 혹은 최대 힙(Max heap)을 이용
# Min heap : 값이 낮은 데이터 먼저 삭제 // Max heap : 값이 큰 데이터 먼저 삭제
# 파이썬의 Priority Queue 방식은 Min heap에 기반함
# Min heap을 Max heap처럼 사굥할 때에는 우선순위에 해당하는 값에 음수부호(-)를
# 붙여서 넣었다가 꺼낸 다음에 (-)를 붙여 원래 값으로 돌리는 방식도 사용 가능.


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


n, m = map(int, input().split())            # n : 노드 갯수, # m : 간선 갯수
start = int(input())                        # start : 시작노드 번호

# 각 노드의 연결정보를 담는 리스트
graph = [[] for i in range(n + 1)]          
for _ in range(m):
    a, b, c = map(int, input().split())     # a → b 일 때, 비용 c
    graph[a].append((b, c))                 # graph의 a인덱스에 (목적지 : b, 비용 : c) 추가
    
distance = [INF] * (n + 1)                  # 거리 테이블 초기화(초기값 : 무한(INF))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))       # 큐에 시작노드 정보(거리, 시작노드 번호) 삽입
    distance[start] = 0                 # 시작노드 거리 테이블 정보 삽입
    while q: # 큐가 빌때까지 반복
        dist, now = heapq.heappop(q)    # 최단 거리 노드 정보 꺼내기
        if distance[now] < dist:        # 이미 처리된 노드일 경우 무시
            continue
        for i in graph[now]:            # 현재 노드와 다른 노드간 거리 탐색
            cost = dist + i[1]
            if cost < distance[i[0]]:   # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

'''
input:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

output:
0
2
3
1
2
4
'''