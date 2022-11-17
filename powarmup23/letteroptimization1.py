"""
basically EK algorithm but on vertices?

bfs

*go through tree for every root (recursive or deque)
*keep track of current flow for each node
*passed on current_flow = min(current_flow, M)
*add to current flow of children (weighted)
*if flow is maxed (ie = M)
dont go further down that branch (already done)
*find indices where M = current_flow (I), done
"""

# abs(I,M) > 1e-4

from collections import deque

class Node:

    def __init__(self, M, children):
        self.M = M
        self.children = children
        self.I = 0


N = int(input())

vertices = []
is_root = [True] * N

for i in range(N):
    description = [int(x) for x in input().split()]
    M = description[0]
    children = dict()
    for i in range(2, len(description), 2):
        # description is 1-indexed :((
        child_index = description[i] - 1
        child_weight = description[i+1] / 100
        children[child_index] = child_weight
        # if is child, then is not root
        is_root[child_index] = False
    vertices.append(Node(M, children))

roots = [i for i, val in enumerate(is_root) if val]
for root in roots:
    vertices[root].I = vertices[root].M

queue = deque(roots)

while queue:
    vertex = vertices[queue.popleft()]
    for child_index, weight in vertex.children.items():
        child = vertices[child_index]
        # if not M == I
        if child.M - child.I > 1e-4:
            child.I += min(vertex.M, vertex.I) * weight
            queue.append(child_index)

out = []

for index, vertex in enumerate(vertices):
    if not vertex.M - vertex.I > 1e-4:
        out.append(str(index + 1))

print(" ".join(out))
