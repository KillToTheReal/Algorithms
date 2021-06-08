'''
Мы выбираем любую вершину и начинаем двигаться по первой смежной вершине
до тех пор пока все следующие вершины не будут посещенными или мы не найдем тот элемент, который искали.
Если все смежные вершины посещены, то мы возвращемся до последнего разветвления и начинаем исследовать его.
'''
def DepthSearch():
  from collections import defaultdict
  class Graph:
      def __init__(self):
        self.graph = defaultdict(list)
        self.search_node = None
        self.is_node_found = False

      def addEdge(self, u, v):
        self.graph[u].append(v)

      def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
          if neighbour == self.search_node:
              print("\nNode found")
              self.is_node_found = True
          if neighbour not in visited and not self.is_node_found:
            res = self.DFSUtil(neighbour, visited)

      def DFS(self, v, search_node):
        visited = set()
        self.search_node = search_node 
        self.DFSUtil(v, visited)

        if not self.is_node_found:
          print("\nNothing found :(")

      def print(self):
        for item in self.graph.items():
          print(item)


  MyGraph = Graph()
  MyGraph.addEdge(0, 8)
  MyGraph.addEdge(0, 2)
  MyGraph.addEdge(2, 1)
  MyGraph.addEdge(1, 2)
  MyGraph.addEdge(2, 0)
  MyGraph.addEdge(2, 3)
  MyGraph.addEdge(3, 3)
  MyGraph.print()
  MyGraph.DFS(4, 3)
  
DepthSearch()

