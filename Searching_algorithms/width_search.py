'''
На вход алгоритма подаётся заданный граф (невзвешенный), и номер стартовой вершины N.
Граф может быть как ориент., так и неориент.

Сам алгоритм можно понимать как процесс "поджигания" графа: на нулевом шаге поджигаем только вершину N. 
На каждом следующем шаге огонь с каждой "горящей" вершины перекидывается на всех её соседей; 
т.е. за одну итерацию алгоритма происходит расширение "кольца огня" в ширину на единицу (отсюда и название алгоритма).
'''
from collections import defaultdict

def broad_search():
  class Graph:
      def __init__(self):
        self.graph = defaultdict(list)

      def addEdge(self,u,v):
        self.graph[u].append(v)

      def BFS(self, s, search_node):
        visited = set()

        queue = []
        queue.append(s)
        visited.add(s)

        while queue:
          s = queue.pop(0)
          print (s, end = " ")
          for node in self.graph[s]:
            if not node in visited:
              queue.append(node)
              visited.add(node)
            if node == search_node:
              print("\nNode found")
              return 0
        print("\nNode not found")

      def print(self):
        for item in self.graph.items():
          print(item)

  g = Graph()
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)
  g.print()
  g.BFS(2, 3)

broad_search()
