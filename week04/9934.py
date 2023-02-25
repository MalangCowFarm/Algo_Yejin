# 완전이진트리
import sys
sys.stdin = open('9934_input.txt')

K = int(input()) # K줄
arr = list(map(int, input().split()))
bi_tr = [[] for _ in range(K)]
# 깊이만큼 빈리스트 일단 선언해줌
cnt = 0 # 깊이 알려줄 cnt

def binary_tree(arr, cnt):
    m = len(arr)//2
    bi_tr[cnt].append(arr[m])

    if len(arr) == 1:
        return
    binary_tree(arr[:m], cnt+1)
    binary_tree(arr[m+1:], cnt+1)

binary_tree(arr, cnt)

for i in bi_tr:
    print(*i)