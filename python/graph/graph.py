from collections import deque 
# we spill it 'd-e-c-k'

class Queue:

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)



class Vertix:

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return self.value


class Edge:

    def __init__(self, vertix, weight=0):
        self.weight = weight
        self.vertix = vertix

    def __str__(self):
        return f"{self.vertix},{self.weight}"

class Graph:

    def __init__(self):
        self.__adj_list = {}
      
    def add_vertix(self,value):
      '''
      Arguments: value
      Returns: The added vertex
      Add a vertex to the graph
      '''
  
      vertix = Vertix(value)
      self.__adj_list[vertix] = []
      return vertix


    def add_edge(self, start_vertix, end_vertix=None, weight=0):
        '''
        Arguments: 2 vertices to be connected by the                     edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        '''
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix, weight)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

  
    def get_vertices(self):
      '''
        Arguments: none
        Returns all of the vertices in the graph as a  
        collection (set, list, or similar)
        Empty collection returned if there are no vertices
      '''
  
      return self.__adj_list.keys()

  
    def size(self):
      return len(self.__adj_list)
  
    def get_neighbors(self,vertix):
      '''
      get neighbors
      A rguments: vertex
      Returns a collection of edges connected to the 
      given vertex
      Include the weight of the connection in the returned collection
      Empty collection returned if there are no vertices
      '''
      # return self.__adj_list[vertix]
      return self.__adj_list.get(vertix, [])
  
    def breadth_first(self,start_vertix):
        """
        Perform a breadth-first traversal of the graph starting from the specified vertex.

        Args:
            start_vertex (Vertex): The vertex from which the traversal should begin.

        Returns:
            list: A list containing the values of the vertices visited during the traversal
                  in the order they were traversed.
        """
    
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.dequeue()

            result.append(current_vertix.value)

            neighbors =self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result

    def depth_first(self,start_vertix):
        """
    Perform a depth-first traversal on the graph starting from a specified vertex.

    Parameters:
        start_vertix (Vertex): The vertex to start the depth-first traversal from.

    Returns:
        list: A list of vertex values representing the traversal order.
    """
        result = []
        visted = set()
        def walk(parent):
            if parent not in visted:
                visted.add(parent)
                result.append(parent.value)
                neighbors =self.get_neighbors(parent)
                for edge in neighbors:
                    neighbor = edge.vertix
                    walk(neighbor)

        walk(start_vertix)
        return result
