from itertools import combinations
from collections import Counter

def flatten(l):
    return [item for sublist in l for item in sublist]

min_area = int(input())
num_sections = int(input())
sections = [int(x) for x in input().split(" ")]
# min_area = 100
# num_sections = 10
# sections = [10] * 10

section_ids = [x for x in range(num_sections)]

combs_ids = list(combinations(section_ids, 2))

prods = [sections[comb[0]] * sections[comb[1]] for comb in combs_ids]

prod_is_big = [s >= min_area for s in prods]

big_combs_ids = [comb_id for i, comb_id in enumerate(combs_ids) if prod_is_big[i]]

overlaps = []
occurances = Counter(flatten(big_combs_ids))
for i, comb_ids in enumerate(big_combs_ids):
    overlaps.append(occurances[comb_ids[0]] + occurances[comb_ids[1]] - 2)

out = 0

while sum(overlaps) != 0:
    overlaps = []
    occurances = Counter(flatten(big_combs_ids))
    for i, comb_ids in enumerate(big_combs_ids):
        overlaps.append(occurances[comb_ids[0]] + occurances[comb_ids[1]] - 2)
    for i, overlap in enumerate(overlaps):
        if overlap == 0:
            out += 1
            overlaps.pop(i)
            big_combs_ids.pop(i)
    if len(overlaps) > 0:
        biggest_overlap = overlaps.index(max(overlaps))
        big_combs_ids.pop(overlaps.index(max(overlaps)))

print(out)
# prods = [comb[0] * comb[1] for comb in combs]
# prod_is_enough = [s >= min_area for s in prods]

# big_combs = [comb for i, comb in enumerate(combs) if prod_is_enough[i]]
# flat_big_combs = flatten(big_combs)

# occurances = Counter(flat_big_combs)
# print(occurances)

# overlaps = []
# for i, comb in enumerate(combs):
#     if prod_is_enough[i]:
#         overlaps.append(occurances[comb[0]] + occurances[comb[1]] - 2)
#     else:
#         overlaps.append(0)


# included = [True] * len(prods)

# def done():
#     for i in range(len(prods)):
#         if included[i] and overlaps[i] != 0:
#             return False
#     return True

# while not done():
#     i = overlaps.index(max(overlaps))


# # print(sum(prod_is_enough))
