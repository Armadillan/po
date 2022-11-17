k = "bcdfghjklmnpqrstvwxz"

sentence = input()

out = sentence[:2]

for char in sentence[2:]:
    if not (out[-2:] == 2 * char and char in k):
        out += char

print(out)
