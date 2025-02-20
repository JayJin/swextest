# Q13. 치킨 배달
# 백준 15686번
# https://www.acmicpc.net/problem/15686

from itertools import combinations

n, m = map(int, input().split())
home, chick = [], []

for i in range(n):
    roadmap = list(map(int, input().split()))
    for j in range(n):
        if roadmap[j] == 1:
            home.append((i, j))
        elif roadmap[j] == 2:
            chick.append((i, j))

# 모든 치킨집 중에서 m개의 치킨집을 뽑은 조합 계산
candidates = list(combinations(chick, m))
print("candidates: ", candidates)

# 거리 계산
distance = []
for k in range(len(chick)):
    dist = 0
    for l in range(len(home)):
        dist += abs(chick[k][0] - home[l][0]) + abs(chick[k][1] - home[l][1])
    distance.append(dist)

# M개 치킨집 선택
selected = []
for o in range(m):
    selected.append(chick.pop(distance.index(max(distance))))    
    distance.pop(distance.index(max(distance)))

# 나머지 치킨집 삭제
for p in chick:
    roadmap[p[0]][p[1]] = 0

# # 최소 거리 계산
# for i in home:
#     dist = []
#     for j in chick:
        


# # 모든 치킨집 중에서 m개의 치킨집을 뽑은 조합 계산
# candidates = list(combinations(chick, m))

# # 치킨 거리의 합을 계산하는 함수
# def get_sum(candidate):
#     result = 0
#     # 모든 집에 대하여
#     for hx, hy in home:
#         # 가장 가까운 치킨집을 찾기
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx - cx) + abs(hy - cy))
#         # 가장 가까운 치킨집까지의 거리를 더하기
#         result += temp
#     # 치킨 거리의 합 반환
#     return result

# # 치킨 거리의 합의 최소를 찾아 출력
# result = 1e9
# for candidate in candidates:
#     result = min(result, get_sum(candidate))

# print(result)


'''
input(1):
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

output(1):
5


input(2):
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

output(2):
10


input(3):
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

output(3):
11


input(4):
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1

output(4):
32

'''