# Q21. 인구 이동
# 백준 16234번
# https://www.acmicpc.net/problem/16234

from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# for _ in area:
#     print(_)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤 데이터 갱신
def process(x, y, index):
    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    union[x][y] = index     # 현재 연합의 번호 할당
    summary = graph[x][y]   # 현재 연합의 전체 인구수
    count = 1       # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 앞에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
    






'''
input(1):
2 20 50
50 30
20 40

output(1):
1

input(2):
2 40 50
50 30
20 40

output(2):
0

input(3):
2 20 50
50 30
30 40

output(3):
1

input(4):
3 5 10
10 15 20
20 30 25
40 22 10

output(4):
2

input(5):
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

output(5):
3


'''