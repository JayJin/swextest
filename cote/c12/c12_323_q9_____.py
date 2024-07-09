# Q9. 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

s = [x for x in list(input())]
bucket = []
bucket_size = 1
cnt = 0

for i in range(len(s)):
    for j in range(1, len(s)):
        if s[i] == s[j]:
            s[i] 
        
            


'''
input(1):
aabbaccc

output(1):
7

input(2):
ababcdcdababcdcd

output(2):
9

input(3):
abcabcdede

output(3):
8

input(4):
abcabcabcabcdededededede

output(4):
14

input(5):
xababcdcdababcdcd

output(5):
17
'''