#OTP GENERATOR


inp = input()


# All the digit in off places
number = [inp[i] for i in range(len(inp)) if i % 2]


ans = ""

found = True

# Sq the digit of odd places
for i in number:
    ans += str(int(i) * int(i))
    if len(ans) >= 4:
        found = True
        break
if found:
    print(ans[:4])
else:
    print(ans)
