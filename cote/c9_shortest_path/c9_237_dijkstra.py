# dijkstra 알고리즘의 기본형
# 시간복잡도가 O(V^2)
# 이는 매번 최단 거리 테이블을 선형적으로(모든 원소를 앞에서부터 하나씩)
# 탐색해야 했기 때문임.

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

visited = [False] * (n + 1)                 # 방문여부 체크목적 리스트 생성(초기값 : False)
distance = [INF] * (n + 1)                  # 거리 테이블 초기화(초기값 : 무한(INF))


def get_smallest_node():                    # 미방문 노드 중 최단거리의 노드 번호 반환
    min_value = INF
    index = 0                               # 최단거리 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:      # 거리테이블에서 최단거리 노드 인덱스 추출
            # min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1]           # 거리테이블의 시작노드 인덱스에 비용정보(j[1] = c) 삽입

    for _ in range(n-1):                # 시작노드 제외한 전체 노드에 대해 반복
        now = get_smallest_node()       # 현재 최단거리 노드 인덱스 변수(now)로 추출/방문처리
        visited[now] = True

        for j in graph[now]:            # 추출한 최단거리 노드와 다른 노드간 거리 탐색
            cost = distance[now] + j[1] # 현재 거리정보에 비용(j[1] = c) 더한 기준 cost 산출
            if cost < distance[j[0]]:   # 기존 거리와 cost 비교하여 거리가 짧으면 update
                distance[j[0]] = cost

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
input : 
6 11
1
1 2 2
1 3 5
1 4 1
2 4 2
2 3 3
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