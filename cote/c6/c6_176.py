# 파이썬 정렬함수 sorted(), .sort
# 데이터 범위가 한정되어 있으며, 더 빠르게 동작해야 하는 경우 계수정렬 사용

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

array.sort()
print(array)


# key를 활용한 정렬
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)