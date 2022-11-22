from dataclasses import dataclass
from copy import deepcopy
from collections import deque

@dataclass
class Dish:
    price: int = 0
    num_people: int = 0
    price_index: int = 0

# friends, dishes, wished unique
n, m, k = (int(i) for i in input().split())

dishes = [Dish() for i in range(m)]

for x in input().split():
    dishes[int(x)-1].num_people += 1

prices = [int(x) for x in input().split()]

for i, c in enumerate(prices):
    dishes[i].price = c

price_indices = {}
price_by_price_index = {}
num_price_inidces = 0
for price in sorted(prices):
    if price not in price_indices:
        price_indices[price] = num_price_inidces
        price_by_price_index[num_price_inidces] = price
        num_price_inidces += 1


for dish in dishes:
    dish.price_index = price_indices[dish.price]

dishes_by_price_index = [list() for index in range(num_price_inidces)]
num_upgrade_targets_by_price_index = [0 for index in range(num_price_inidces)]
num_upgrade_sources_by_price_index = [0 for index in range(num_price_inidces)]

for dish in dishes:
    dishes_by_price_index[dish.price_index].append(dish)
    if dish.num_people == 0:
        num_upgrade_targets_by_price_index[dish.price_index] += 1
    elif dish.num_people > 1:
        num_upgrade_sources_by_price_index[dish.price_index] += dish.num_people - 1

#TODO:
# for each source index,
#save queue of higher index targetst
# go backwoards over price indices and put all targets iterated so far into a
# queue for each source iterated over


targets = deque()
targets_by_source = {}
for i in range(num_price_inidces-1, -1, -1):

    if num_upgrade_sources_by_price_index[i] > 0:
        targets_by_source[i] = deque(targets)
    if num_upgrade_targets_by_price_index[i] > 0:
        targets.appendleft(i)


for dish in dishes:
    if dish.num_people:
        k -= 1

"""
get all possible targets for upgrades
and all possible sources
and match them

for each source index,
save queue of higher index targets
that makes diff lookup constant time for each source index,
so O(n) in total (for each source index)
"""


def perform_match():
    """
    perform match, decrementing and incrementing appropriate counters in targets and sources
    decrement k
    return cost of match

    if no available matches, return 0
    """
    global k
    # (source, target, price_difference)
    best = (None, None, 0)
    for i in range(num_price_inidces):
        if num_upgrade_sources_by_price_index[i]:
            target = targets_by_source[i][0] if targets_by_source[i] else None
            while target is not None and not num_upgrade_targets_by_price_index[target]:
                targets_by_source[i].popleft()
                target = targets_by_source[i][0] if targets_by_source[i] else None
            if target is not None:
                price_difference = price_by_price_index[target] - price_by_price_index[i]
                if price_difference < best[2] or best[2] == 0:
                    best = (i, target, price_difference)

    if best[0] is None:
        return 0
    num_upgrade_sources_by_price_index[best[0]] -= 1
    num_upgrade_targets_by_price_index[best[1]] -= 1
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
