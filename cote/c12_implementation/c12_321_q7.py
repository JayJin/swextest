# Q7. 럭키 스트레이트
# 백준 18406
# https://www.acmicpc.net/problem/18406

n = [int(x) for x in list(input())]

if sum(n[:int((len(n)+1)//2)]) == sum(n[int((len(n)+1)//2):]):
    print("LUCKY")
else:
    print("READY")
    
'''
input(1):
123402

output(1):
LUCKY

input(2):
7755

output(2):
READY
'''