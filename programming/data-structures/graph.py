class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbour in self.graph[vertex]:
                self.graph[neighbour].remove(vertex)
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=" \n")

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=" \n")
                visited.add(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] if neighbor not in visited])

    def __str__(self):
        return str(self.graph)


graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# Add edges
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")

# Print the graph
print("Graph:", graph)

# Depth-First Search (DFS)
print("DFS starting from vertex A:")
graph.dfs("A")

# Breadth-First Search (BFS)
print("BFS starting from vertex A:")
graph.bfs("A")
