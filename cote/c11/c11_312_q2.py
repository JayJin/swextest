s = [int(x) for x in list(input())]

result = s[0]

for i in range(len(s)-1):
    if result + s[i+1] >= result * s[i+1]:
        result += s[i+1]
    else:
        result *= s[i+1]

print(result)

'''
input(1):
02984

output(1):
576

input(2):
567

output(2):
210
'''