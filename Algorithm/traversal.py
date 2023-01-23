# dfs/bfs 와 같은 그래프 순회를 구현해본다.
# graph =
# {1:[2, 3, 4], 2:[5], 3:[5], 4:[], 5:[6,7], 6:[], 7:[3],}
class Traversal():
    graph = {}

    def __init__(self, graph={}):
        self.graph = graph

    def recursive_dfs(self, v, discovered=[]):
        discovered.append(v)
        print(v)
        for w in self.graph[v]:
            if w not in discovered:
                discovered = self.recursive_dfs(w, discovered)
        # 방문했던 정점을 누적하기 위해서 리턴한다.
        return discovered

    def iterative_dfs(self, v):
        stack = [v]
        discovered = []

        while stack:
            v = stack.pop()
            # if v not in discovered:
            discovered.append(v)
            print(v)
            for w in self.graph[v]:
                if w not in discovered:
                    stack.append(w)
        print(discovered)

    def iterative_bfs(self, v):
        discovered = [v]
        queue = [v]

        while queue:
            v = queue.pop(0)
            print(v)
            for w in self.graph[v]:
                if w not in discovered:
                    queue.append(w)
                    discovered.append(w)
        print(discovered)

    # 이하 코드보다 위의 분기가 더 깔끔하다.
    def _iterative_bfs(self, v):
        discovered = []
        queue = [v]

        while queue:
            v = queue.pop(0)
            if v not in discovered:
                for w in self.graph[v]:
                    if w not in discovered:
                        queue.append(w)
                discovered.append(v)
                print(v)
        print(discovered)


# 실행
graph = {1: [2, 3, 4],
         2: [5],
         3: [5],
         4: [],
         5: [6, 7],
         6: [],
         7: [3], }

traversal = Traversal(graph)
print('---------recursive_dfs---------')
traversal.recursive_dfs(1, [])
print('---------iterative_dfs---------')
traversal.iterative_dfs(1)
print('---------iterative_bfs---------')
traversal.iterative_bfs(1)
