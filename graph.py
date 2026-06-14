import heapq

from Vertex import Vertex


class Graph:

    def __init__(self):
        self.wg = {}

    class VertexDist:

        def __init__(self, vertex, distance):
            self.vertex = vertex
            self.distance = distance

        def get_vertex(self):
            return self.vertex

        def get_distance(self):
            return self.distance

        def __lt__(self, other):
            return self.distance < other.distance

    class Edge:

        def __init__(self, v1, v2, distance):
            self.v1 = v1
            self.v2 = v2
            self.distance = distance

        def get_v1(self):
            return self.v1

        def get_v2(self):
            return self.v2

        def get_distance(self):
            return self.distance

        def __eq__(self, other): # python equaivalent of java.equasls
            if not isinstance(other, Graph.Edge):
                return False

            return (
                self.distance == other.distance
                and self.v1 == other.v1
                and self.v2 == other.v2
            )

        def __str__(self):
            return f"{self.v1} -> {self.v2} ({self.distance})"

    def changeVertexStrength(self, name, newStrength):
        tempVertex = Vertex(name, newStrength)
        if tempVertex not in self.wg: # only works cuz we check using name in Vertex.__eq__
            return
        else:
            for vertex in self.wg:
                if vertex == tempVertex:
                    vertex.strength = newStrength

            # gotta change all the neighbors as well
            for vertex in self.wg:
                for edge in self.wg[vertex]:
                    if edge.get_v2() == tempVertex:
                        edge.v2.strength = newStrength
            

    def add_edge(self, v1, v2, distance):
        edge1 = self.Edge(v1, v2, distance)
        edge2 = self.Edge(v2, v1, distance)

        if v1 not in self.wg:
            self.wg[v1] = []

        if v2 not in self.wg:
            self.wg[v2] = []

        if edge1 not in self.wg[v1]:
            self.wg[v1].append(edge1)
            self.wg[v2].append(edge2)

       

    def get_vertices(self):
        return self.wg.keys()

    def get_edges(self):
        edges = []

        for vertex in self.wg:
            for edge in self.wg[vertex]:
                edges.append(edge)

        return edges

    def get_neighbors(self, vertex):

        if vertex not in self.wg:
            return []

        neighbors = []

        for edge in self.wg[vertex]:
            neighbors.append(edge.get_v2())

        return neighbors

    def get_distance(self, v1, v2):

        if v1 not in self.wg:
            return float("inf")

        for edge in self.wg[v1]:
            if edge.get_v2() == v2:
                return edge.get_distance()

        return float("inf")

    def print_neighbors(self, vertex):

        if vertex not in self.wg:
            print(vertex + " []")
            return

        print(vertex)

        for edge in self.wg[vertex]:
            print("   ", edge)

  

    def bfs(self, start):
        from collections import deque
        visited = set()
        queue = deque([start])
        visited.add(start)
        output = []

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                output.append(curr)
                for neighbor in self.get_neighbors(curr):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            output.append("new level")

        return output
    
    def degree_centrality(self):
        output = {}
        verticies = self.get_vertices()
        for i in verticies:
            output[i] = len(self.get_neighbors(i)) * i.strength/100
        
        output2 = sorted(output.keys(), key=lambda x: output[x], reverse=True)
        return output2

    def djk(self, start, end):

        visited = set()
        shortest = {}
        pred = {}

        queue = []

        pred[start] = None

        for v in self.get_vertices():

            if v == start:
                shortest[v] = 0
            else:
                shortest[v] = float("inf")

        curr = start

        while len(visited) < len(self.wg):

            close = self.get_neighbors(curr)

            for c in close:

                if c in visited:
                    continue

                distance = self.get_distance(curr, c)*(c.strength/100) + shortest[curr] # using c.strength cuz we are "going" to c as a new trainign method

                if distance < shortest[c]:
                    shortest[c] = distance
                    pred[c] = curr

                temp = self.VertexDist(c, shortest[c])

                heapq.heappush(queue, temp)

            visited.add(curr)

            if not queue:
                break

            curr = heapq.heappop(queue).get_vertex()

        if end not in pred:
            return []

        temp = end
        output = []
        while temp:
            output.insert(0, temp)
            temp = pred[temp]

        return output




