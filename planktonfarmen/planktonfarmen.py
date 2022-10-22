min_area = int(input())
num_sections = int(input())
sections = [int(x) for x in input().split(" ")]

sections.sort()

min_mul = [min_area / section for section in sections]

offset = -1
out = 0
for section in sections:
    if section >= min_mul[offset]:
        out += 1
        offset -= 1

#could check if (index of section < num_sections - out) to avoid
#integer division, but no need :)

print(out // 2)
