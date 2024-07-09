import sys

n = int(input())
nlist = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
mlist = list(map(int, sys.stdin.readline().rstrip().split()))
# n = int(input())
print(n)

def bi_search(nlist, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if nlist[mid] == target:
        return mid
    elif nlist[mid] > target:
        return bi_search(nlist, target, start, mid-1)
    else:
        return bi_search(nlist, target, mid+1, end)

for i in mlist:
    result = bi_search(nlist, i, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
'''
input : 
5
8 3 7 9 2
3
5 7 9

output :
no yes yes
'''