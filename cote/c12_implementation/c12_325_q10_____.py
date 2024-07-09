# Q10. 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

key = input()
lock = input()

def rotation(matrix):
    matrix[i][j] = matrix[n]

class move(): 
    def up(self, matrix):
        matrix[i][j] = matrix[i+1][j]
    def down(self, matrix):
        matrix[i][j] = matrix[i-1][j]
    def left(self, matrix):
        matrix[i][j] = matrix[i][j+1]
    def right(self, matrix):
        matrix[i][j] = matrix[i][j-1]


'''
key
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]

lock
[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

result
true
'''