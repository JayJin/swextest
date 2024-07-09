# Q15. 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

# 최단거리가 k인 모든 도시의 번호 오름차순으로
# 없을 경우 -1 출력

# 그래프에서 모든 간선의 거리가 동일할 때 → 너비우선탐색(BFS)

# n : 도시수, m : 도로수, k : 거리정보, x : 출발도시 번호
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0     # 출발 도시의 거리는 0으로 설정

q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력    
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

    
'''
input(1):
4 4 2 1
1 2
1 3
2 3
2 4

output(2):
4

input(2):
4 3 2 1
1 2
1 3
1 4

output(2):
-1

input(3):
4 4 1 1
1 2
1 3
2 3
2 4

output(3):
2
3
'''



