"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exost")# TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        
        visited = set()
        
        while q.size > 0:
            v = q.dequeue()
            
            if v not in visited:
                visited.add(v)
                print(v)
                
                for next_vartex in self.get_neighbors(v):\
                    q.enqueue(next_vartex)  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        
        visited = set()
        
        while s.size > 0:
            v = s.pop()
            
            if v not in visited:
                visited.add(v)
                print(v)
                
                for next_vartex in self.get_neighbors(v):
                    s.push(next_vartex)  # TODO

    def dft_recursive(self, starting_vertex, visited):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)
          # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH To the Starting Vertex ID
        q = Queue()
        path = [starting_vertex]
        # create a set to store visited vertices
        q.enqueue(path)

        visited = set()

        # while the queue is not empty
        while q.size > 0:
            current = q.dequeue()
            # dequeue the first PATH
            # grab the last vertex from the Path
            current_node = current[-1]

            # check if the vertex has not been visited
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                # is this vertex the target?
            if current_node == destination_vertex:
                return current
                    # return the path
                # mark it as visited

                # then add A Path to its neighbors to the back of the queue
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                    
                # make a copy of the path
                copy = current[:]
                # append the neighbor to the back of the path
                copy.append(neighbor)
                # enqueue out new path
                q.enqueue(copy)

        return None  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        # create a set to store visited vertices
        s.push(path)

        visited = set()

        # while the queue is not empty
        while s.size > 0:
            current = s.pop()
            # dequeue the first PATH
            # grab the last vertex from the Path
            current_node = current[-1]

            # check if the vertex has not been visited
            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                # is this vertex the target?
            if current_node == destination_vertex:
                return current
                    # return the path
                # mark it as visited

                # then add A Path to its neighbors to the back of the queue
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                    
                # make a copy of the path
                copy = current[:]
                # append the neighbor to the back of the path
                copy.append(neighbor)
                # enqueue out new path
                s.push(copy)

        return None  # TODO  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
