n = int(input())
coin = sorted(list(map(int, input().split())))
cnt_list = [0]*(sum(coin) + 1)

for i in coin:
    cnt_list[i] = 1
    cnt = cnt_list[i]
    for j in range(len(coin)):
        cnt += coin[i+1]
        
print(cnt_list)

'''
input:
5
3 2 1 1 9

output:
8
'''