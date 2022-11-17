min_area = int(input())
num_sections = int(input())
sections = [int(x) for x in input().split(" ")]

sections.sort()

out = 0
while len(sections) > 1:
    if sections[0] * sections[-1] >= min_area:
        sections.pop()
        sections.pop(0)
        out += 1
    else:
        sections.pop(0)

print(out)
