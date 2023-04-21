import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n과목수 m선수조건수
graph = [1] * (n+1) # 결과 반환 리스트
arr = [[] for _ in range(n+1)] # 조건 입력 리스트 [[], [2, 3], [5], [], [5], [], []]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(1, n+1):
    for j in arr[i]:
        graph[j] = max(graph[j], graph[i]+1)

print(*graph[1:])