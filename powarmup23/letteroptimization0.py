#adjecency matrix with edge weigths as values
#Edmonds-Karp algorithm from https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
#modified to return  residual graph
# need to add supersource and supersink
#get number of edges with values > 0 from residual graph

import collections

class Graph:
    '''
    This class represents a directed graph using
    adjacency matrix representation.
    '''

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.row = len(graph)

    def bfs(self, s, t, parent):
        '''
        Returns true if there is a path from
        source 's' to sink 't' in residual graph.
        Also fills parent[] to store the path.
        '''

        # Mark all the vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    # Returns the maximum flow from s to t in the given graph
    def edmonds_karp(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

N = int(input())
# +2 for source and sink nodes
adjecency_graph = [[0] * (N+2) for n in range(N+2)]

#source is index -2, sink is index -1
source = -2
sink = -1

is_root = [True] * N
M_values = [0] * N

edges = {n:list() for n in range(N)}

for i in range(N):
    description = [int(x) for x in input().split()]
    M = description[0]
    M_values[i] = M
    if description[1] == 0:
        adjecency_graph[i][sjink] = M
        adjecency_graph[sink][i] = -M
    else:
        for j_i in range(2, len(description), 2):
            # j is 1-indexed in input, so subtract 1
            j = description[j_i]-1
            edges[i].append(j)
            adjecency_graph[i][j] = M * description[j_i+1] / 100
            adjecency_graph[j][i] = -M * description[j_i+1] / 100
            is_root[j-1] = False

for i, val in enumerate(is_root):
    if val == True:
        adjecency_graph[source][i] = M_values[i]
        adjecency_graph[i][source] = -M_values[i]

graph = Graph(adjecency_graph)
graph.edmonds_karp(source, sink)

out = set()

# I - M > 10**-4

for key, val in edges.items():
    if sum(adjecency_graph[key][j] for j in val) < 1e-4:
        out.add(key+1)

for i, val in enumerate(is_root):
    if val:
        out.add(i+1)

print(" ".join(str(x) for x in sorted(out)))
