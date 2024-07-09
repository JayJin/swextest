# Q16. 연구소
# https://www.acmicpc.net/problem/14502

import copy

n, m = map(int, input().split())

graph = []  # 초기 맵 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))

dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]

result = 0

def spread_virus(graph, x, y):
    for [ddx, ddy] in dxy:
        nx, ny = x + ddx, y + ddy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            spread_virus(graph, nx, ny)

def get_score(graph):
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    if count == 3:
        temp_graph = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 2:
                    spread_virus(temp_graph, i, j)
        result = max(result, get_score(temp_graph))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(count + 1)
                graph[i][j] = 0

dfs(0)
print(result)





'''
input(1):
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

output(1):
27

input(2):
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

output(2):
9

input(3):
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

output(3):
3

'''