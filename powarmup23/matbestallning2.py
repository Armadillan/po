from collections import deque
from dataclasses import dataclass

@dataclass
class IntPtr:
    val: int

# friends, dishes, wished unique
n, m, k = (int(i) for i in input().split())

people_per_dish = [0] * m
for x in input().split():
    people_per_dish[int(x)-1] += 1

price_per_dish = [int(x) for x in input().split()]

price_indices = {}
price_by_price_index = []
num_price_inidces = 0
for price in sorted(price_per_dish):
    if price not in price_indices:
        price_indices[price] = num_price_inidces
        price_by_price_index.append(price)
        num_price_inidces += 1

num_upgrade_targets_by_price_index = [0 for index in range(num_price_inidces)]
num_upgrade_sources_by_price_index = [0 for index in range(num_price_inidces)]

for i in range(m):
    price = price_per_dish[i]
    people = people_per_dish[i]
    if people == 0:
        num_upgrade_targets_by_price_index[price_indices[price]] += 1
    elif people > 1:
        num_upgrade_sources_by_price_index[price_indices[price]] += people - 1

targets = deque() # first target by price_index
latest_target = IntPtr(None)
for i in range(num_price_inidces-1, -1, -1):
    targets.appendleft(latest_target)
    if num_upgrade_targets_by_price_index[i]:
        latest_target = IntPtr(i)

for i in range(m):
    if people_per_dish[i]:
        k -= 1

def perform_match():
    global k
    res = 0
    best = (None, None, 0)
    for i in range(num_price_inidces):
        if num_upgrade_sources_by_price_index[i]:
            target = targets[i].val
            if target is not None:
                price_difference = price_by_price_index[target] - price_by_price_index[i]
                if price_difference < best[2] or best[2] == 0:
                    best = (i, target, price_difference)

    if best[0] is None:
        return 0
    num_upgrade_sources_by_price_index[best[0]] -= 1
    num_upgrade_targets_by_price_index[best[1]] -= 1
    if num_upgrade_targets_by_price_index[best[1]] == 0:
        targets[best[0]] = targets[targets[best[0]].val]
    k -= 1
    return best[2]

out = 0
while k > 0:
    res = perform_match()
    if not res:
        print(-1)
        exit()
    out += res
print(out)


"""
find best target for every source, get list of ascending cost
start from highest source, and go down ?
print(sum(list[:num_needed_swaps]))
"""
