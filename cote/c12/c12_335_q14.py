# Q14. 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

# '제한조건'을 보았을 때, weak 리스트와 dist 리스트의 길이가 매우 작음  → 완전탐색 가능
# 투입해야 하는 친구 수의 최솟값 / 전체 친구수(최대 8)
# → 모든 친구를 무작위로 나열하는 모든 순열(Permutation)의 개수 계산 8P8 = 8! = 40,320 (계산 가능)
# 따라서 친구를 나열하는 모든 경우의 수를 각각 확인하여 친구를 최소 몇 명 배치하면 되는지 계산

# 다만 문제에서는 취약한 지점들이 원형으로 구성
# → 원형으로 구성된 데이터 처리시 문제풀이를 간단히 하기 위해 길이를 2배로 늘려서 원형을 1자형태로 하면 유리
# 각 친구를 나열하는 모든 경우의수 n!
# 각 경우에 대해서 모든 취약한 지점을 검사할 수 있는지 확인

from itertools import permutations


n = int(input())                            # 외벽의 길이
weak = list(map(int, input().split()))      # 취약지점의 위치(오름차순으로 정렬되어 주어짐)
dist = list(map(int, input().split()))      # 각 친구가 한 시간동안 이동할 수 있는 거리


def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer


solution(n, weak, dist)     # 보내야 하는 친구 수의 최솟값


'''
n	weak	     dist	    result
12	1 5 6 10	 1 2 3 4	2
12	1 3 4 9 10	 3 5 7	    1

'''