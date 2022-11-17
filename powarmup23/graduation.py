from collections import deque

n, m, k = (int(x) for x in input().split())

rows = [input() for _ in range(n)]

classes_in_columns = deque([set(x) for x in zip(*rows)])

next_deque = deque()

out = 0

while classes_in_columns:
    out += 1
    classes = classes_in_columns.pop()
    done = False
    while not done:
        done = True
        for _ in range(len(classes_in_columns)):
            next_classes = classes_in_columns.pop()
            if not next_classes & classes:
                next_deque.appendleft(next_classes)
            else:
                classes |= next_classes
                done = False

        classes_in_columns = next_deque
        next_deque = deque()


print(out)
