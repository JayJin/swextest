INF = int(1e9)

n, m = map(int, input().split())     # 회사 개수 N, 경로 개수 M

route = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n+1):
    route[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())    # 연결된 회사
    route[a][b] = 1
    route[b][a] = 1
    
x, k = map(int, input().split())        # x : 목적지, k : 경유지

# Floyd Warshal Algorithm 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            route[a][b] = min(route[a][b], route[a][k] + route[k][b])

# 경유지까지
if route[1][k] + route[k][x] < INF :
    print(route[1][k] + route[k][x])
else:
    print(-1)


    

'''
input(1):
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

output(1):
3

input(2):
4 2
1 3
2 4
3 4

output(2):
-1
'''