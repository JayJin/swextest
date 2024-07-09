# Q25. 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stages = stages.sort(reversed=True)
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
    
    # 실패율을 기준으로 각 스테이지 내림차순 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    
    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer

# input1:
solution(5, [2, 1, 2, 6, 2, 4, 3, 3])

# input2:
solution(4, [4, 4, 4, 4, 4])

# output1:
# [3, 4, 2, 1, 5]

# output2:
# [4, 1, 2, 3]