brackets = input()

stack = []

openBracket = {"(", "{", "["}
closeBracket = {")": "(", "}": "{", "]": "["}

ans = 0

for i, j in enumerate(brackets):

    if j in openBracket:
        stack.append(j)
    else:
        if not stack:
            ans = i + 1
            break

        k = stack.pop()

        if k != closeBracket[j]:
            ans = i + 1

            break


if ans != 0:
    print(ans)
elif stack:
    print(i + 2)
