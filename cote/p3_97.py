n, m = map(int, input().split())

min_list = []
for i in range(n):
    min_list.append(min(list(map(int, input().split()))))

result = max(min_list)
print(result)

