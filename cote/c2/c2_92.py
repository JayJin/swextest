n, m, k = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
# 또는 list(map(int, input().split())).sort()

if m < 3:
    result = num_list[-1] * m
else:
    f = m // 4
    s = m % 4
    result = num_list[-1]*f*3 + num_list[-2]*f + num_list[-1]*s

print(result)