# 시간복잡도는 O(N^3)
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
n, m = map(int, input().split())        # 노드, 간선 갯수 입력

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 그래프에 간선에 대한 정보를 입력
for a in range(1, n + 1):   # a → a 일 때, 비용 0
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):  # a → b 일 때, 비용 c
    a, b, c = map(int, input().split())     # a → b 일 때, 비용 c
    graph[a][b] = c

# Floyd Warshal Algorithm 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")        # 도달 불가시
        print(graph[a][b], end=" ")           # 도달 가능시 거리를 출력
    print()

'''
input :
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

output:
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
'''