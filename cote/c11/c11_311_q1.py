n = int(input())
member = sorted(list(map(int, input().split())))
print(member)
groups = []
cnt = 0
while member:
    groups.append([])
    a = max(member)
    print("cnt: ",cnt)
    print("a: ", a)
    for j in range(a):
        if len(member) != 0:
            b = member.pop()
            groups[cnt].append(b)
    cnt += 1

print(groups)
print(len(groups))

'''
input:
5
2 3 1 2 2
10
2 3 4 4 1 2 3 4 5 2

output:
2
'''