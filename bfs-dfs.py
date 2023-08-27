from typing import List


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.visited: bool = False
        self.adjacent: List[Node] = []


class Graph:
    def __init__(self, graph) -> None:
        self.key_node_dict = self.init_graph(graph)

    def init_graph(self, graph):
        nodes = {}
        # Nodes 생성
        for key in graph.keys():
            nodes[key] = Node(key)
        # Adjacent 삽입
        for key in graph.keys():
            for edge in graph[key]:
                nodes[key].adjacent.append(nodes[edge])

        return nodes

    def get_node(self, key: str) -> Node | None:
        if self.key_node_dict[key] != None:
            return self.key_node_dict[key]

    def clean_visited(self) -> None:
        for key in self.key_node_dict.keys():
            self.key_node_dict[key].visited = False

    def dfs(self, start: str, container: List[str]) -> None:
        curr_node = self.get_node(start)

        # start node가 없으면 return
        if curr_node == None:
            return

        # 방문처리
        curr_node.visited = True
        container.append(start)

        # 방문하지 않은 인접 노드 검색 후 dfs 수행.
        for next in curr_node.adjacent:
            if next.visited == False:
                self.dfs(next.key, container)

    def bfs(self, start: str, container: List[str]) -> None:
        start_node = self.get_node(start)
        if start_node == None:
            return

        # 1. 시작 노드를 큐에 삽입하고 방문처리한다.
        q = [start_node]
        start_node.visited = True
        container.append(start_node.key)

        # 4. 2, 3번을 반복한다.
        while len(q) != 0:
            # 2. 큐에서 하나의 노드를 꺼낸다.
            curr_node = q.pop(0)

            # 3. 해당 노드에 연결된 노드 중 방문하지 않은 노드를 큐에 삽입하며 방문처리한다.
            for node in curr_node.adjacent:
                if node.visited == False:
                    q.append(node)
                    node.visited = True
                    container.append(node.key)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    g = Graph(graph)

    # bfs
    bfs_path = []
    g.bfs("A", bfs_path)
    g.clean_visited()

    # dfs
    dfs_path = []
    g.dfs("A", dfs_path)

    print(bfs_path)
    print(dfs_path)
