from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj_list = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, weight: int = 1):
        self.vertices.add(u)
        self.vertices.add(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        return self.adj_list[vertex]
    
    def get_vertices(self):
        return self.vertices


def create_graph(edges: List[Tuple], directed: bool = False) -> Graph:
    graph = Graph(directed)
    for edge in edges:
        if len(edge) == 3:
            u, v, weight = edge
            graph.add_edge(u, v, weight)
        else:
            u, v = edge
            graph.add_edge(u, v, 1)
    return graph


def dfs(graph: Graph, start_vertex, visited: Optional[Set] = None) -> List:
    if visited is None:
        visited = set()
    
    result = []
    if start_vertex not in visited:
        visited.add(start_vertex)
        result.append(start_vertex)
        
        for neighbor, _ in graph.get_neighbors(start_vertex):
            if neighbor not in visited:
                result.extend(dfs(graph, neighbor, visited))
    
    return result


def bfs(graph: Graph, start_vertex) -> List:
    visited = set([start_vertex])
    queue = deque([start_vertex])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def dijkstra(graph: Graph, start_vertex) -> Tuple[Dict, Dict]:
    distances = {vertex: float('inf') for vertex in graph.get_vertices()}
    predecessors = {vertex: None for vertex in graph.get_vertices()}
    distances[start_vertex] = 0
    
    pq = [(0, start_vertex)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_neighbors(current_vertex):
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return distances, predecessors


def get_path(predecessors: Dict, start_vertex, end_vertex) -> Optional[List]:
    if end_vertex not in predecessors:
        return None
    
    path = []
    current = end_vertex
    
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    path.reverse()
    return path if path[0] == start_vertex else None