import sys
sys.stdin = open('4789_input.txt')

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    ans = 0
    arr = list(map(int, input()))
    for i in range(len(arr)):
        if arr[i] != 0:
            if cnt < i:
                ans += i - cnt
                cnt += i - cnt
        cnt += arr[i]
    print(f'#{tc} {ans}')