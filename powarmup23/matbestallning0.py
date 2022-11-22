from dataclasses import dataclass

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
num_price_inidces = 0
for price in sorted(prices):
    if price not in price_indices:
        price_indices[price] = num_price_inidces
        num_price_inidces += 1

for dish in dishes:
    dish.price_index = price_indices[dish.price]

dishes_by_price_index = {index: list() for index in range(num_price_inidces)}

for dish in dishes:
    dishes_by_price_index[dish.price_index].append(dish)

unique = 0
for dish in dishes:
    if dish.num_people:
        unique += 1

out = 0

def perform_best_upgrade():
    """
    subtract one from some num_people where num_people > 1
    add one to somewhere where num_people = 0
    such that
    the difference in price is minimal but > 0
    and increment unique
    if no upgrades can be made, return None
    """
    global unique
    # tuple of (index_from, index_to, cost, num_people)
    best_upgrade = (None, None, dishes_by_price_index[num_price_inidces-1][0].price)

    for from_dish in dishes:

        if from_dish.num_people > 1:

            for i in range(from_dish.price_index+1, num_price_inidces):
                cost = dishes_by_price_index[i][0].price - from_dish.price
                if cost >= best_upgrade[2]:
                    break
                for to_dish in dishes_by_price_index[i]:
                    if to_dish.num_people == 0:
                        best_upgrade = (from_dish, to_dish, cost)
                        break
    if best_upgrade[0] is not None:
        unique += 1
        best_upgrade[0].num_people -= 1
        best_upgrade[1].num_people += 1
        return best_upgrade[2]
    return None


while unique < k:

    best_upgrade = perform_best_upgrade()

    if best_upgrade is None:
        print(-1)
        exit()
    out += best_upgrade

print(out)

"""
get all possible targets for upgrades
and all possible sources
and match them
highest source, match with lowest available target
"""
