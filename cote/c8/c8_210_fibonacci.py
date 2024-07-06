def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

# 시간복잡도 O(2^n)으로 컴퓨팅 손실이 매우 큼