# Q24. 안테나
# https://www.acmicpc.net/problem/18310

n = int(input())
nx = list(map(int, input().split()))

INF = 1e9

a_dist = [INF for _ in range(max(nx)+1)]

for i in range(1, max(nx)+1):
    dist = 0
    for j in nx:
        dist += abs(i-j)
    a_dist[i] = dist


print(a_dist.index(min(a_dist)))


############################33
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()

# # 중간값(median)을 출력
# print(a[(n - 1) // 2])


'''
input:
4
5 1 7 9

output:
5
'''