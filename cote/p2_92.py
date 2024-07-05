n, m, k = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

if m < 3:
    result = num_list * m
else:
    m % 4