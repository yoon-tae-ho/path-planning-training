import queue

from find import find

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def bfs_with_list(start) -> None:
    # 1. 시작 노드를 큐에 삽입하고 방문처리한다.
    q = [start]
    visited = [start]

    # 4. 2, 3번을 반복한다.
    while len(q) != 0:
        # 2. 큐에서 하나의 노드를 꺼낸다.
        curr = q[0]
        del q[0]

        # 3. 해당 노드에 연결된 노드 중 방문하지 않은 노드를 큐에 삽입하며 방문처리한다.
        for node in graph[curr]:
            if find(node, visited) == -1:
                q.append(node)
                visited.append(node)

    print(visited)


def bfs_with_queue(start) -> None:
    # 1. 시작 노드를 큐에 삽입하고 방문처리한다.
    q = queue.Queue()
    q.put(start)
    visited = [start]

    # 4. 2, 3번을 반복한다.
    while q.qsize() != 0:
        # 2. 큐에서 하나의 노드를 꺼낸다
        curr = q.get()

        # 3. 해당 노드에 연결된 노드 중 방문하지 않은 노드를 큐에 삽입하며 방문처리한다.
        for node in graph[curr]:
            if find(node, visited) == -1:
                q.put(node)
                visited.append(node)

    print(visited)


if __name__ == "__main__":
    bfs_with_list("F")
    bfs_with_queue("F")
