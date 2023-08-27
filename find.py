from typing import Sequence, TypeVar


T = TypeVar("T")  # for generic


# Sequence에 target이 존재하는지 검색.
# 존재한다면 index를, 그렇지 않다면 -1을 리턴.
def find(target: T, list: Sequence[T], reverse: bool = False) -> int:
    list = reversed(list) if reverse else list
    for index, item in enumerate(list):
        if item == target:
            return index
    return -1
