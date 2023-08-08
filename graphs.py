class Graph:
    """
    Construct a Graph
    """

    # Initialize
    def __init__(self) -> None:
        self.adj_list = {}
    
    # Add vertex
    def add_vertex(self, vertex: int) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    # Add edge
    def add_edge(self, v1: int, v2: int) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    # Remove edge
    def remove_edge(self, v1: int, v2: int) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    # Remove vertex
    def remove_vertex(self, vertex: int) -> bool:
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
    # Print vertices
    def print_graph(self) -> None:
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

my_graph = Graph()