n = int(input())
directions = list(input().split())

pointer_x = 1
pointer_y = 1

for i in range(len(directions)):
    if directions[i] == 'R':
        if pointer_y < n:
            pointer_y += 1           
    elif directions[i] == 'L':
        if pointer_y != 1:
            pointer_y -= 1
    elif directions[i] == 'U':
        if pointer_x != 1:
            pointer_x -= 1
    else:
        if pointer_x < n:
            pointer_x +=1

print(pointer_x, pointer_y)