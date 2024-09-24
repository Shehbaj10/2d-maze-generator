from typing import List
from maze.util import Coordinates
from maze.graph import Graph

class AdjListGraph(Graph):
    """
    Represents an undirected graph. Please complete the implementations of each method.
    """

    def __init__(self):
        # Initialising an empty adjacency list
        self.maze_adjacent_list1 = {}

    def addVertex(self, label: Coordinates):
        # Adding a vertex to the graph
        if label not in self.maze_adjacent_list1:
            # Initialise an empty set to store the neighbors 
            self.maze_adjacent_list1[label] = set()

    def addVertices(self, vertLabels: List[Coordinates]):
        # Adding multiple vertices to the graph
        for label in vertLabels:
            # Add each vertex individually
            self.addVertex(label)

    def addEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates, addWall: bool = False) -> bool:
        # Adding an edge between two vertices
        if maze_vertices_1 in self.maze_adjacent_list1 and maze_vertices_2 in self.maze_adjacent_list1:
            # Update the adjacency lists of both vertices 
            self.maze_adjacent_list1[maze_vertices_1].add(maze_vertices_2)
            self.maze_adjacent_list1[maze_vertices_2].add(maze_vertices_1)
            return True
        else:
            return False

    def updateWall(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates, wallStatus: bool) -> bool:
        # Updating the wall status between two vertices
        if maze_vertices_1 in self.maze_adjacent_list1 and maze_vertices_2 in self.maze_adjacent_list1:
           
            if wallStatus:
                self.maze_adjacent_list1[maze_vertices_1].add(maze_vertices_2)
                self.maze_adjacent_list1[maze_vertices_2].add(maze_vertices_1)
            else:
                self.maze_adjacent_list1[maze_vertices_1].discard(maze_vertices_2)
                self.maze_adjacent_list1[maze_vertices_2].discard(maze_vertices_1)
            return True
        else:
            return False

    def removeEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        # Removing an edge between two vertices
        if maze_vertices_1 in self.maze_adjacent_list1 and maze_vertices_2 in self.maze_adjacent_list1:
            # Remove the edge from both vertices' 
            if maze_vertices_2 in self.maze_adjacent_list1[maze_vertices_1]:
                self.maze_adjacent_list1[maze_vertices_1].remove(maze_vertices_2)
                self.maze_adjacent_list1[maze_vertices_2].remove(maze_vertices_1)
                return True
            else:
                return False
        else:
            return False

    def hasVertex(self, label: Coordinates) -> bool:
        # Checking if a vertex exists in the graph
        return label in self.maze_adjacent_list1

    def hasEdge(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        # Checking if an edge exists between two vertices
        if maze_vertices_1 in self.maze_adjacent_list1 and maze_vertices_2 in self.maze_adjacent_list1:
            return maze_vertices_2 in self.maze_adjacent_list1[maze_vertices_1]
        else:
            return False

    def getWallStatus(self, maze_vertices_1: Coordinates, maze_vertices_2: Coordinates) -> bool:
        # Getting the wall status between two vertices
        if maze_vertices_1 in self.maze_adjacent_list1 and maze_vertices_2 in self.maze_adjacent_list1:
            return maze_vertices_2 in self.maze_adjacent_list1[maze_vertices_1]
        else:
            return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        # Getting the neighbors of a vertex
        if label in self.maze_adjacent_list1:
            return list(self.maze_adjacent_list1[label])
        else:
            return []
