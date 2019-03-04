"""
Simple graph implementation
"""
from support import Queue, Stack

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v_id):
        if v_id in self.vertices:
            raise IndexError("That vertex already exists")
        else:
            self.vertices[v_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("At least one of those vertices does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("At least one of those vertices does not exist")

    def bft(self, starting_v_id):
        q = Queue()
        q.enqueue(starting_v_id)
        visited = set()
        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    q.enqueue(neighbor)

    def dft(self, starting_v_id):
        s = Stack()
        s.push(starting_v_id)
        visited = set()
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    s.push(neighbor)


graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('4', '6')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('7', '6')
print(graph.vertices)
graph.dft('1')