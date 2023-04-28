import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100000)

"""

"""
def find(depth):
    global ans
    
    if depth == 11:
        ans = max(ans, sum(ans_lst))
        return
    
    for i in range(11):
        if visited[i]:
            continue
        if arr[depth][i]:
            visited[i] = 1
            ans_lst.append(arr[depth][i])
            find(depth+1)
            ans_lst.pop()
            visited[i] = 0

for _ in range(int(input())): # tc
    arr = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    ans = 0
    ans_lst = []
    
    find(0)
    print(ans)