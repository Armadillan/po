# O(n) solution i think

s = input()

l = len(s) // 2

s *= 2

out = current = s[:l].count("B")

for i in range(1, l*2):
    if s[i-1] == "B":
        current -= 1
    if s[i-1+l] == "B":
        current += 1

    if current > out:
        out = current

print(out)
