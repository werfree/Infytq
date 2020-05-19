n = input()


def substring(n):
    ans = ""

    l = len(n)
    if l < 3:
        return(-1)
    for i in range(0, l - 2):
        s = set()
        s.add(n[i])
        s.add(n[i + 1])
        s.add(n[i + 2])
        if len(s) > 2 and len(s) > len(ans):
            ans = (n[i] + n[i + 1] + n[i + 2])
    return ans if ans != "" else -1


print(substring(n))
