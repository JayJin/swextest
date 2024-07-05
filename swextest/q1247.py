T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    town = int(input())
    dist = list(map(int, input().split()))

    coord = []
    cdlist = dist[:2]
    hdlist = dist[2:4]

    coord.append(cdlist)
    for i in range(int(len(dist)/2)-2):
        coord.append(dist[2*i+4:2*i+6])

    dmat = []
    for j in range(len(coord)-1):
        temp = []
        for k in range(len(coord)-1):
            temp.append(abs(coord[j][0]-coord[k][0])+abs(coord[j][1]-coord[k][1]))
        dmat.append(temp)

    print(dmat)

    stack = []
    dist_cnt = 0
    pointer_r = 0
    pointer_c = 0
    while True:
        if pointer_r == 0:
            stack.append(pointer_r+1)
            dist_cnt += dmat[pointer_r][pointer_c+1]
            while pointer_c <= len(coord):
                pointer_c += 1
