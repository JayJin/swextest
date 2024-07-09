def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:      # 찾고자 하는 원소와 동일할 경우
            return i + 1    # 현재 위치 반환(인덱스는 0부터이므로 add 1)

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))