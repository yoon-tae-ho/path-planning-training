from typing import Tuple, List, TypeVar, Union
from heapq import heappush, heappop, heapify

from find import find


Coordinate = TypeVar("Coordinate", bound=Tuple[int, int])


class Node:
    def __init__(
        self, curr: Coordinate, end: Coordinate, parent_node: Union["Node", None]
    ) -> None:
        self.coord: Coordinate = curr
        self.parent_node = parent_node
        self.id = self.create_id(curr)
        self.H_score = self.get_H_score(end)
        self.G_score = self.get_G_score()
        self.F_score = self.H_score + self.G_score

    # Node instance로도 find 함수를 사용할 수 있도록 "==" 연산자를 재지정.
    def __eq__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return self.id == other.id
        return False

    # heap에서 Node의 크기 비교를 위해 F_score를 사용하기 위해 "<" 연산자를 재지정.
    def __lt__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return self.F_score < other.F_score
        return False

    # Manhattan distance
    def get_H_score(self, end: Coordinate) -> int:
        return (
            (abs(self.coord[0] - end[0]) + abs(self.coord[1] - end[1]))
            if self.parent_node is not None
            else 0
        )

    def get_G_score(self) -> int:
        return self.parent_node.G_score + 1 if self.parent_node is not None else 0

    @staticmethod
    def create_id(coord: Coordinate) -> str:
        return str(coord[0]) + str(coord[1])

    @staticmethod
    def get_parent_list(node: "Node") -> List["Node"]:
        if node.parent_node is None:
            return [node.coord]
        return [*Node.get_parent_list(node.parent_node), node.coord]


def find_shortest_path(
    start: Coordinate, end: Coordinate, obstacles: List[Coordinate]
) -> List[Coordinate]:
    edges: List[Coordinate] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    open_list: List[Node] = []  # minimum heap
    closed_list: List[Node] = []

    # start Node를 open_list에 추가
    start_node = Node(start, end, None)
    heappush(open_list, start_node)

    while True:
        # 1. open_list에서 F_score가 최소인 애를 closed_list로 옮긴다.
        curr_node = heappop(open_list)
        closed_list.append(curr_node)

        # 2. 옮겨진 노드와 인접한 노드들 생성 후 closed_list에 없는 노드들을 open_list에 추가.
        for edge in edges:
            new_coord: Coordinate = (
                curr_node.coord[0] + edge[0],
                curr_node.coord[1] + edge[1],
            )
            new_node: Node = Node(new_coord, end, curr_node)

            # obstacles 혹은 closed_list에 존재하는 node는 추가하지 않음.
            if (
                find(new_coord, obstacles) != -1
                or find(new_node, closed_list, True) != -1
            ):
                continue

            # open_list에 존재하지 않는 node라면 heappush.
            # 그렇지 않으면 G_Score를 비교하여 작은 값 적용.
            open_list_idx = find(new_node, open_list)
            if open_list_idx == -1:
                heappush(open_list, new_node)
            else:
                if open_list[open_list_idx].G_score > new_node.G_score:
                    open_list[open_list_idx] = new_node

        # 3. 2번 마지막 과정에서 heap의 정렬 기준인 F_score가 갱신되었으므로 다시 heapify.
        heapify(open_list)

        # 4. 1~3 반복하다 end Node가 closed_list에 추가되면 종료.
        if closed_list[-1].id == Node.create_id(end):
            break

    # start - end path 리턴
    return Node.get_parent_list(closed_list[-1])


if __name__ == "__main__":
    start: Coordinate = (0, 0)
    end: Coordinate = (100, 100)
    obstacles: List[Coordinate] = [(3, 0), (5, 1), (5, 2), (5, 3), (9, 4)]

    print(find_shortest_path(start, end, obstacles))
