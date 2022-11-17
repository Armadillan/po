N = input()

l = len(N)

N = int(N)

value = int("1" * l)
if value > N:
    l -= 1
    value = int("1" * l)

out = 0

while N > 0:
    out += N // value
    N %= value
    if l > 1:
        l -= 1
        value = int("1" * l)


print(out)
