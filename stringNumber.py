

def stringNumber(n):
    n = set(i for i in n if i.isdigit())
    n = list(n)
    n.sort(reverse=True)
    l = len(n)
    if l == 0:
        return -1
    if int(n[l - 1]) % 2 == 0:
        return n
    for i in range(l - 2, -1, -1):
        if int(n[i]) % 2 == 0:
            n[l - 1], n[i] = n[i], n[l - 1]
            return n
    return -1


n = input()
ans = stringNumber(n)
if ans == -1:
    print(ans)
else:
    k = 0
    for i in ans:
        k = (k * 10) + int(i)
    print(k)
