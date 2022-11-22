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

upgrades = []

for i in range(num_price_inidces):
    while num_upgrade_sources_by_price_index[i]:
        target = targets[i].val
        if target is not None:
            price_difference = price_by_price_index[target] - price_by_price_index[i]
            upgrades.append(price_difference)
            num_upgrade_sources_by_price_index[i] -= 1
            num_upgrade_targets_by_price_index[target] -= 1
            if num_upgrade_targets_by_price_index[target] == 0:
                targets[i] = targets[targets[i].val]
        else:
            break

if len(upgrades) < k:
    print(-1)
else:
    print(sum(sorted(upgrades)[:k]))
