# Q17. 경쟁적 전염
# 백준 18405번
# https://www.acmicpc.net/problem/18405

# 너비 우선 탐색 사용!(BFS)

from collections import deque

# 입력
n, k = map(int, input().split())    # n : 시험관 크기 / k : 바이러스 종류

# 시험관 map
data = []       # 바이러스 정보 저장
graph = []      # 전체 보드 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))   # 종류/시간/위치X/위치Y
data.sort()
q = deque(data)

s, x, y = map(int, input().split()) # s:경과시간, x, y : 탐색할 바이러스 위치

# 바이러스 증식 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s_que, x_que, y_que = q.popleft()
    # 정확히 S초가 지나거나 큐가 빌 때까지 반복
    if s_que == s:
        break
    for i in range(4):
        nx, ny = x_que+dx[i], y_que+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s_que+1, nx, ny))

print(graph[x-1][y-1])

    


'''
input(1):
3 3
1 0 2
0 0 0
3 0 0
2 3 2

output(1):
3

input(2):
3 3
1 0 2
0 0 0
3 0 0
1 2 2

output(2):
0
'''