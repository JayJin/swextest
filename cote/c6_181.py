n = int(input())

scores = []
for i in range(n):
    name, s = input().split()
    scores.append((name, int(s)))

def setting(data):
    return data[1]

# result = sorted(scores, key=lambda student: student[1])
result = sorted(scores, key=setting)     # reverse=False : 작은 순서대로

for i in range(len(result)):
    print(result[i][0], end=' ')