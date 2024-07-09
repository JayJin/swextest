# Q3. 문자열 뒤집기
# 백준 1439
# https://www.acmicpc.net/problem/1439



s = [int(x) for x in list(input())]

cnt = 0
result = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
result = (cnt + 1) // 2
print(result)

'''
input:
0001100

output:
1
'''