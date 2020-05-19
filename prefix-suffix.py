n = input()

i = 0
j = len(n)
iEnd = j // 2 - 1
jStart = iEnd + 1
j -= 1


ans = 0
while iEnd >= i and jStart <= j:
    print(n[iEnd], n[j])
    if n[iEnd] == n[j]:
        ans += 1
        iEnd -= 1
        j -= 1
    else:
        iEnd -= 1

print(ans)
