from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for neighbor in sorted(self.graph[node]):
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def bfs(self, start, order='left'):
        visited = [False] * (max(self.graph) + 1)
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft() if order == 'left' else queue.pop()
            print(node, end=' ')

            for neighbor in sorted(self.graph[node]):
                if not visited[neighbor]:
                    queue.append(neighbor) if order == 'left' else queue.appendleft(neighbor)
                    visited[neighbor] = True

    def detect_cycles(self):
        visited = [False] * (max(self.graph) + 1)
        stack = []
        result = []

        def dfs_util(node):
            nonlocal visited, stack, result

            visited[node] = True
            stack.append(node)

            for neighbor in self.graph[node]:
                if neighbor in stack:
                    result.append(stack[stack.index(neighbor):] + [neighbor])
                elif not visited[neighbor]:
                    dfs_util(neighbor)

            stack.pop()

        for node in self.graph:
            if not visited[node]:
                dfs_util(node)

        if result:
            print("\nCycles in the graph:")
            for cycle in result:
                print(''.join(map(str, cycle)))

    def is_bipartite(self, start):
        colors = [-1] * (max(self.graph) + 1)
        colors[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbor in self.graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False  # Graph is not bipartite

        return True  # Graph is bipartite

# Example usage:
g = Graph()
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(4, 2)

print("DFS:")
g.dfs(1, [False] * 5)  # Assuming there are 4 nodes in the graph

print("\nBFS (left order):")
g.bfs(1, 'left')

print("\nBFS (right order):")
g.bfs(1, 'right')

g.detect_cycles()

if g.is_bipartite(1):
    print("\nThe graph is bipartite.")
else:
    print("\nThe graph is not bipartite.")
