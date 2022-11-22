from collections import deque

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

upgrade_sources_by_index = [0] * num_price_inidces
upgrade_targets_by_index = [0] * num_price_inidces

for dish, people in enumerate(people_per_dish):
    index = price_indices[price_per_dish[dish]]
    if people == 0:
        upgrade_targets_by_index[index] += 1
    elif people > 1:
        upgrade_sources_by_index[index] += people -1

upgrades = []

target_indices = [i for i in range(num_price_inidces) if upgrade_targets_by_index[i]]
source_indices = deque(i for i in range(num_price_inidces) if upgrade_sources_by_index[i])

source_queue = deque()

for target_index in target_indices:
    while source_indices and source_indices[0] < target_index:
        source_queue.append(source_indices.popleft())
    while upgrade_targets_by_index[target_index] and source_queue:
        matches = min(upgrade_sources_by_index[source_queue[-1]], upgrade_targets_by_index[target_index])
        upgrade_sources_by_index[source_queue[-1]] -= matches
        upgrade_targets_by_index[target_index] -= matches
        upgrades.extend(
            [price_by_price_index[target_index]-price_by_price_index[source_queue[-1]]] * matches
        )
        if not upgrade_sources_by_index[source_queue[-1]]:
            source_queue.pop()


for i in range(m):
    if people_per_dish[i]:
        k -= 1

if len(upgrades) < k:
    print(-1)
else:
    print(sum(sorted(upgrades)[:k]))
