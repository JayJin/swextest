food_times = list(map(int, input().split()))
k = int(input())
cnt = k
blanked = []
i = 0

while True:
    if i == len(food_times):
        i = 0
    else:
        if cnt>0 and food_times[i] > 0:
            food_times[i] -= 1
            cnt -= 1
            print(f'i: {i} cnt: {cnt} food_times: {food_times} 1')
        elif food_times[i] == 0:
            blanked.append(i)
            print(f'i: {i} cnt: {cnt} food_times: {food_times} 2')
        elif cnt == 0:
            print(f'i: {i} cnt: {cnt} food_times: {food_times} 3')
            if i in blanked:
                print("continued")
                continue
            else:
                print(i + 1)
                break
        i += 1
        
'''
input:
3 1 2
5

output:
1
'''
            