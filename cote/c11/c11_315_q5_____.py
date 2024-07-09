# Q5. 볼링공 고르기

n, m = map(int, input().split())
weights = list(map(int, input().split()))

cnt = 0
for i in range(len(weights)):
    for j in range(i+1, len(weights), 1):
        if weights[i] != weights[i+1]:
            cnt += 1
            
print(cnt)

'''
input(1):
5 3
1 3 2 3 2

output(1):
8

input(2):
8 5
1 5 4 3 2 4 5 2

output(2):
25


'''