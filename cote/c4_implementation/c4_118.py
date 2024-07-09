n, m = map(int, input().split())
chr_x, chr_y, chr_d = map(int, input().split())

mmap = []
for i in range(n):
    mmap.append(list(map(int, input().split())))

dir_types = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # up, right, down, left
dir_state = chr_d
pos_state = [chr_x, chr_y]

print(pos_state)
print(type(pos_state))

print([pos_state[0], pos_state[1]-1])
# fine road
cnt = 1
while True:
    if (dir_state == 0)&(pos_state[1] != 1)&(mmap[pos_state[0]: pos_state[1]-1] != 1):
        pos_state += dir_types[dir_state]
        cnt += 1
        print("up")
    elif (dir_state == 3)&(pos_state[0] != 1)&(mmap[pos_state[0]-1: pos_state[1]] != 1):
        pos_state += dir_types[dir_state]
        cnt += 1
        print("left")
    elif (dir_state == 2)&(pos_state[1] != -1)&(mmap[pos_state[0]: pos_state[1]+1] != 1):
        pos_state += dir_types[dir_state]
        cnt += 1
        print("down")
    elif dir_state == 1&(pos_state[0] != -1)&(mmap[pos_state[0]+1: pos_state[1]] != 1):
        pos_state += dir_types[dir_state]
        cnt += 1
        print("right")
    else:
        print("종료")
        break


