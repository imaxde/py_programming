import heapq
from collections import Counter


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(freq: dict[str, int]) -> Node:
    heap = [Node(f, c) for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(a.freq + b.freq, left=a, right=b))
    return heap[0]


def build_table(node: Node, prefix="", table=None) -> dict[str, str]:
    if table is None:
        table = {}
    if node.char is not None:
        table[node.char] = prefix or "0"
        return table
    build_table(node.left, prefix + "0", table)
    build_table(node.right, prefix + "1", table)
    return table


def encode(msg: str) -> tuple[str, dict[str, str]]:
    # считаем частоту появления подстроки
    freq = Counter(msg)
    tree = build_tree(freq)
    table = build_table(tree)
    encoded = "".join(table[ch] for ch in msg)
    return encoded, table


def decode(encoded: str, table: dict[str, str]) -> str:
    reverse = {v: k for k, v in table.items()}
    result = []
    buf = ""
    for bit in encoded:
        buf += bit
        if buf in reverse:
            result.append(reverse[buf])
            buf = ""
    return "".join(result)

