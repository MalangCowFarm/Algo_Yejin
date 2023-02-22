import sys
sys.stdin = open('input.txt')

def DFS(start = 1):
    stack = [start]
    visited = [0] * (N+1)
    cnt = 1

    while stack:
        start = stack.pop()

        if visited[start] == 0:
            visited[start] = cnt
            cnt += 1

            for next in range(1, N+1):
                if data[start][next] == 1 and visited[next] == 0:
                    stack.append(next)

    return visited[1:]

N, M, R = map(int, input().split())
data = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N):
    S, R = map(int, input().split())
    data[S][R] = 1
    data[R][S] = 1


print(DFS())