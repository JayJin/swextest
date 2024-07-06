n, k = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

for i in range(k):
    if min(array_a) >= max(array_b):
        print("끝내기")
        break
    a_min_idx = array_a.index(min(array_a))
    b_max_idx = array_b.index(max(array_b))
    array_a[a_min_idx], array_b[b_max_idx] = array_b[b_max_idx], array_a[a_min_idx]

print(sum(array_a))
