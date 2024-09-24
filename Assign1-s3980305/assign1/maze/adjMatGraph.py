from typing import List
from maze.util import Coordinates
from maze.graph import Graph

class AdjMatGraph(Graph):
    """
    Represents an undirected graph using an adjacency matrix with a dictionary of sets.
    """

    def __init__(self):
        """
        Initializes the graph with an empty dictionary to store vertices and their neighbors.
        """
        self.maze_adjacent_matrix1 = {}

    def addVertex(self, label: Coordinates):
        """
        Adds a vertex to the graph.
        """
        if label not in self.maze_adjacent_matrix1:
            # Initialising an empty set to store the neighbors 
            self.maze_adjacent_matrix1[label] = set()

    def addVertices(self, vertLabels: List[Coordinates]):
        """
        Adds multiple vertices to the graph.
        """
        for label in vertLabels:
            # Adding each vertex 
            self.addVertex(label)

    def addEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates, addWall: bool = False) -> bool:
        """
        Adds an edge between two vertices in the graph.
        """
        if maze_vertices_1 in self.maze_adjacent_matrix1 and maze_vertices_2 in self.maze_adjacent_matrix1:
            # Adding the edge between both vertices 
            self.maze_adjacent_matrix1[maze_vertices_1].add((maze_vertices_2, addWall))
            self.maze_adjacent_matrix1[maze_vertices_2].add((maze_vertices_1, addWall))
            return True
        else:
            return False

    def updateWall(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates, wallStatus: bool) -> bool:
        """
        Updates the wall status between two vertices.
        """
        if maze_vertices_1 in self.maze_adjacent_matrix1 and maze_vertices_2 in self.maze_adjacent_matrix1:
            # Updating  the wall status between the two vertices
            self.maze_adjacent_matrix1[maze_vertices_1].discard((maze_vertices_2, not wallStatus))
            self.maze_adjacent_matrix1[maze_vertices_1].add((maze_vertices_2, wallStatus))
            self.maze_adjacent_matrix1[maze_vertices_2].discard((maze_vertices_1, not wallStatus))
            self.maze_adjacent_matrix1[maze_vertices_2].add((maze_vertices_1, wallStatus))
            return True
        else:
            return False

    def removeEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        """
        Removes an edge between two vertices in the graph.
        """
        if maze_vertices_1 in self.maze_adjacent_matrix1 and maze_vertices_2 in self.maze_adjacent_matrix1:
            # Removing the edge between both vertices 
            self.maze_adjacent_matrix1[maze_vertices_1].discard((maze_vertices_2, False))
            self.maze_adjacent_matrix1[maze_vertices_1].discard((maze_vertices_2, True))
            self.maze_adjacent_matrix1[maze_vertices_2].discard((maze_vertices_1, False))
            self.maze_adjacent_matrix1[maze_vertices_2].discard((maze_vertices_1, True))
            return True
        else:
            return False

    def hasVertex(self, label: Coordinates) -> bool:
        """
        Checks if the graph contains a vertex with the given label.
        """
        return label in self.maze_adjacent_matrix1

    def hasEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        """
        Checks if there is an edge between two vertices in the graph.
        """
        if maze_vertices_1 in self.maze_adjacent_matrix1 and maze_vertices_2 in self.maze_adjacent_matrix1:
            # Check if the edge exists 
            return (maze_vertices_2, True) in self.maze_adjacent_matrix1[maze_vertices_1] or (maze_vertices_2, False) in self.maze_adjacent_matrix1[maze_vertices_1]
        else:
            return False

    def getWallStatus(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        """
        Gets the status of the wall between two vertices.
        """
        if maze_vertices_1 in self.maze_adjacent_matrix1 and maze_vertices_2 in self.maze_adjacent_matrix1:
            # Get the wall status between the two vertices from the adjacency matrix
            return (maze_vertices_2, True) in self.maze_adjacent_matrix1[maze_vertices_1]
        else:
            return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        """
        Returns a list of neighboring vertices of the given vertex.
        """
        if label in self.maze_adjacent_matrix1:
            # Return the neighboring vertices of the given vertex 
            return [vertex for vertex, _ in self.maze_adjacent_matrix1[label]]
        else:
            return []
