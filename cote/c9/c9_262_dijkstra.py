import heapq
INF = int(1e9)


n, m, start = map(int, input().split())     # n : 노드수, m : 루트 수, c : 시작위치

# graph는 연결정보 // distance는 거리정보
graph = [[] for _ in range(n+1)]
distance = [INF] * (n + 1) 

for _ in range(m):
    x, y, z = map(int, input().split())      # x → y(cost z)
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0       # 도달할 수 있는 노드의 개수
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)        # 시작노드 제외(count-1)



'''
input:
3 2 1
1 2 4
1 3 2

output:
2 4
'''
    
