# Q20. 감시피하기
# https://www.acmicpc.net/problems/18428
from itertools import combinations
import copy

n = int(input())
clsmap = []

for _ in range(n):
    clsmap.append(list(input().split()))

for i in range(len(clsmap)):
    print(clsmap[i])

std = []
tcr = []
blk = []

for j in range(n):
    for k in range(n):
        if clsmap[j][k] == "X":
            blk.append([j, k])
        elif clsmap[j][k] == "T":
            tcr.append([j, k])
        elif clsmap[j][k] == "S":
            std.append([j, k])

obstacles = list(combinations(blk, 3))


# 장애물 검사
def check_up(map, tx, ty):
    if ty-1 < 0:
        return 0
    elif map[tx][ty-1] == 'X':
        check_up(map, tx, ty-1)
    elif map[tx][ty-1] == 'O':
        return 0
    elif map[tx][ty-1] == 'S':
        return 1
    return 0

def check_down(map, tx, ty):
    if ty+1 >= n:
        return 0
    elif map[tx][ty+1] == 'X':
        check_down(map, tx, ty+1)
    elif map[tx][ty+1] == 'O':
        return 0
    elif map[tx][ty+1] == 'S':
        return 1
    return 0

def check_left(map, tx, ty):
    if tx-1 < 0:
        return 0
    if map[tx-1][ty] == 'X':
        check_left(map, tx-1, ty)
    elif map[tx-1][ty] == 'O':
        return 0
    elif map[tx-1][ty] == 'S':
        return 1
    return 0

def check_right(map, tx, ty):
    if tx+1 >= n:
        return 0
    if map[tx+1][ty] == 'X':
        check_right(map, tx+1, ty)
    elif map[tx+1][ty] == 'O':
        return 0
    elif map[tx+1][ty] == 'S':
        return 1
    return 0

    
# 장애물 설치 후 검사
result = 0
for i in range(len(obstacles)):
    temp_map = copy.deepcopy(clsmap)
    for [j, k] in obstacles[i]:
        temp_map[j][k] = 'O'
        for [tx, ty] in tcr:
            up = check_up(temp_map, tx, ty)
            do = check_down(temp_map, tx, ty)
            le = check_left(temp_map, tx, ty)
            ri = check_right(temp_map, tx, ty)
            result = result + up + do + le + ri


if result != 0:
    print("NO")
else:
    print("YES")

    
    
# print(result)
    
    
'''
input(1):
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

output(1):
YES

input(2):
4
S S S T
X X X X
X X X X
T T T X

output(2):
NO

'''