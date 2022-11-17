#gå baklänges-lösning

n = input()

heights = [int(x) for x in input().split()]

min_height = heights[-1]
index = len(heights) - 2
while heights[index] >= min_height:
    min_height = heights[index]
    index -= 1

missing = min_height - heights[index]

while index > 0:
    index -= 1
    min_height += missing
    missing = min_height - heights[index]
    if missing < 0:
        missing = 0
        min_height = heights[index]

print(missing)
