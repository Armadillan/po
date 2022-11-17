"""
O(n^2) solution counting Bs in all sublists of circular linked list
"""

s = input()
l = int(len(s) / 2)

s = s * 2

out = 0

for i in range(l*2):
    n = s[i:i+l].count("B")
    if n > out:
        out = n

print(out)
