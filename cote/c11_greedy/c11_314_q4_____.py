# Q4. 만들 수 없는 금액

n = int(input())
coin = sorted(list(map(int, input().split())))
cnt_list = [0]*(sum(coin) + 1)


for i in coin:
    cnt_list[i] = 1
    cnt = cnt_list[i]
    for j in range(len(coin)):
        cnt += coin[i+1]
        
print(cnt_list)


######################################################################33
########## ▼▼▼▼▼▼▼▼ 정답 ▼▼▼▼▼▼▼▼▼
target = 1 ################

for x in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)



'''
input:
5
3 2 1 1 9

output:
8
'''