# Q11. 뱀
# https://www.acmicpc.net/problem/3109
# 백준 3190번

# 큐를 사용할 문제인지 꼭 판단할 것!!

from collections import deque


n = int(input())        # 보드의 크기 N x N
k = int(input())        # 사과의 개수 k

board = [[0 for _ in range(n)] for _ in range(n)]

# 사과의 위치 (행, 열)
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1     ##### 인덱스를 0부터

l = int(input())        # 방향 변환 횟수

cd = []     # 방향전환 정보를 담을 리스트
for _ in range(l):
    x, c = input().split()        # x : 경과시간, c : 회전 방향(90도)
    cd.append((int(x), c))

# body = [[1, 1], [1, 1]]
# length = 1

# dx = [-1, 0, 1, 0]  # left, up, right, down
# dy = [0, 1, 0, -1]

# time_count = 0


dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]
direction = 0  # 초기 방향 우측


# 뱀의 초기 위치
snake = deque([(0, 0)])  # 뱀의 몸통 위치를 저장하는 큐 (머리가 앞쪽)
time = 0  # 경과 시간
cd_idx = 0  # 방향 변환 정보 인덱스


while True:
    time += 1
    head_x, head_y = snake[0]
    new_head_x = head_x + dx[direction]
    new_head_y = head_y + dy[direction]
    
    # 벽에 부딪히거나 자신의 몸에 부딪히는 경우 게임 종료
    if not (0 <= new_head_x < n and 0 <= new_head_y < n) or (new_head_x, new_head_y) in snake:
        break
    
    # 사과가 있는 경우
    if board[new_head_x][new_head_y] == 1:
        board[new_head_x][new_head_y] = 0           # 사과 먹기
        snake.appendleft((new_head_x, new_head_y))  # 머리 추가
    else:
        snake.appendleft((new_head_x, new_head_y))  # 머리 추가
        snake.pop()     # 꼬리 제거
        
    # 방향변환이 필요한 시간인지 확인
    if cd_idx < l and time == cd[cd_idx][0]:
        if cd[cd_idx][1] == 'L':
            direction = (direction - 1) % 4     # -1 % 4 = 3
        else:
            direction = (direction + 1) % 4
        cd_idx += 1








# def rotation(c):
#     global c_idx
#     if c == "L":
#         c_idx -= 1 if c != 0 else 3
#     else:
#         c_idx += 1 if c != 3 else 0

# for i in range(len(cd)):
#     for x, c in cd:
#         for f in range(int(x)):
#             if body[0][0]+dx[c_idx] >= n or body[0][1]+dy[c_idx] >= n:
#                 print("game over")
#                 print("time: ", time_count)
#                 break
#             elif [body[0][0]+dx[c_idx], body[0][1]+dy[c_idx]] in body:
#                 print("game over")
#                 print("time: ", time_count)
#                 break
#             elif board[body[0][0]+dx[c_idx]][body[0][1]+dy[c_idx]] == 0:
#                 body[0][0] += dx[c_idx]
#                 body[0][1] += dy[c_idx]
#                 for i in range(len(body)):
#                     body[i][0] += body[i-1][0]
#                     body[i][1] += body[i-1][1]
#                 time_count += 1
#                 print("time: ", time_count)
#             # 사과를 먹었을 경우
#             elif board[body[0][0]+dx[c_idx]][body[0][1]+dy[c_idx]] == 1:
#                 body.insert(0, [body[0][0] + dx[c_idx], body[0][1] + dy[c_idx]])
#                 board[body[0][0]+dx[c_idx]][body[0][1]+dy[c_idx]] = 0
#                 time_count += 1
#                 print("time: ", time_count)
#         rotation(c)
            
    



'''
input(1):
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

output(1):
9

input(2):
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

output(2):
21

input(3):
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

output(3):
13

'''