# insertion sort는 selection sort보다 실행시간 측면에서 상대적으로 효율적
# 시간복잡도는 selection sort와 동일하게 O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):       # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)