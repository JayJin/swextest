# Q29. 공유기 설치
# 백준 2110번
# https://www.acmicpc.net/problem/2110

# '가장 인접한 두 공유기 사이의 거리'의 최댓값
# 이진 탐색으로 '가장 인접한 두 공유기 사이의 거리'를 조절해가며
# 매 순간 실제로 공유기를 설치하여 c보다 많은 개수로 공유기를 설치할 수 있는지를 체크

n, c = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while (start<=end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n):       # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:      # c개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        start = mid + 1
        result = mid        # 최적의 결과를 저장
    else:       # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)



'''
input:
5 3
1
2
8
4
9

output:
3
'''