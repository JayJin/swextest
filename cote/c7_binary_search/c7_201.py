import sys

n, m = sys.stdin.readline().rstrip().split()
mlist = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

def bi_search(mlist, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    cake = list(map(lambda x : x-mid, mlist))
    size = sum(x for x in cake if x >= 0)
    # size = 0
    # for x in cake:
    #     if x >= 0:
    #         size += 1

    print(f"mid: {mid} | cakesize: {size}")
    if size == target:
        return mid
    if size > target:
        return bi_search(mlist, target, mid+1, end)
    else:
        return bi_search(mlist, target, start, mid-1)

result = bi_search(mlist, int(m), 0, max(mlist))

print(result)
'''
input:
4 6
19 15 10 17

output:
15
'''