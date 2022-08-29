t = int(input())
for _ in range(t):
    stk = []
    s = input()
    vps = True

    for ch in s:
        if ch == '(':
            stk.append('(')
        if ch == ')':
            if stk:
                stk.pop()
            elif not stk:
                vps = False
                break
    if not stk and vps:
        print('YES')
    elif stk or not vps:
        print('NO')
