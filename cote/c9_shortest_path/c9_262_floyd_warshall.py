INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    x, y, z = map(int, input().split())      # x → y(cost z)
    graph[x][y] = z

# Floyd Warshall Algorithm
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
time = 0
for j in range(1, n+1):
    for k in range(1, n+1):
        if graph[j][k] != 0 and graph[j][k] < INF:
            cnt += 1
            if time < graph[j][k]:
                time = graph[j][k]

print(f"{cnt} {time}")
            

'''
input:
3 2 1
1 2 4
1 3 2

output:
2 4
'''