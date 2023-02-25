# 트럭

import sys
sys.stdin = open('13335_input.txt')

# n 건너는 트럭 수 w 다리길이, L 다리 최대하중
n, w, L = map(int, input().split())
truck = list(map(int, input().split())) #7 4 5 6

queue = [0] * w # [0 0]
cnt = 0

while queue:
    cnt += 1
    queue.pop(0)
    if truck:
        if sum(queue) + truck[0] > L:
            queue.append(0)
        else:
            queue.append(truck.pop(0))
print(cnt)