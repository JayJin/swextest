s = sorted([x for x in list(input())])

cnt = 0
num = 0
for i in range(len(s)):
    if s[i].isdigit():
        cnt += int(s[i])
        num = i
    else:
        print(s[i], end='')
print(cnt)

'''
input(1):
K1KA5CB7

output(1):
ABCKK13

input(2):
AJKDLSI412K4JSJ9D

output(2):
ADDIJJJKKLSS20
'''

# 숫자 판별: isdecimal( ), isdigit( ), isnumeric( )
# 문자열 판별 : isalpha( )