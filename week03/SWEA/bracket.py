T = int(input())
for tc in range(1, T+1):
    words = input()
    stack = []
    cnt = 1

    for word in words:
        if word == '(' or word =='{':
            stack.append(word)
        elif word == ')' or word =='}':
            if len(stack) == 0:
                cnt = 0
                break
            elif word == ')' and stack.pop() == '{':
                cnt = 0
                break
            elif word == '}' and stack.pop() == '(':
                cnt = 0
                break
    if len(stack):
        cnt = 0

    print(f'#{tc} {cnt}')