# Q19. 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888
# 첫째 줄에 최댓값, 둘째 줄에 최솟값 출력
from itertools import combinations, permutations

n = int(input())

nums = list(map(int, input().split()))  # 일련의 숫자
cals = list(map(int, input().split()))  # 활용 가능한 연산자 숫자 (+, -, ×, ÷)

cal_list = []

for i in range(len(cals)):
    for j in range(cals[i]):
        cal_list.append(i)

sum_list = []
perm_set = set(permutations(cal_list, len(cal_list)))

def calculation(a, b, j):
    if j == 0:
        result = a + b
    elif j == 1:
        result = a - b
    elif j == 2:
        result = a * b
    elif j == 3:
        result = int(a / b)
    return result

for set in perm_set:
    result = 0
    for i in range(len(nums)):
        if i == 0:
            result += nums[i]
        else:
            result = calculation(result, nums[i], set[i-1] )
    sum_list.append(result)

print(max(sum_list))
print(min(sum_list))

'''
input(1):
2
5 6
0 0 1 0

output(1):
30
30

input(2):
3
3 4 5
1 0 1 0

output(2):
35
17

input(3):
6
1 2 3 4 5 6
2 1 1 1

output(3):
54
-24
'''