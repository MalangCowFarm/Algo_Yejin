import sys
sys.stdin = open('6190_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # n개의 정수
    arr = list(map(int, input().split()))
    arr.sort()

    print(arr)