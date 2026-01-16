# heapを使用して下記の問題を解決する。
# heapは、常に優先度の高い要素を効率よく取り出すためのデータ構造である。
# Stack（後入れ先出し・LIFO）や Queue（先入れ先出し・FIFO）とは異なり、
# Heapは優先度付きキューとして動作する。
# 本問題では、サイズkの最小ヒープを維持し、
# 新しい要素が追加されるたびにヒープのサイズを調整することで、
# 常にk番目に大きい値を取得できるようにする。

import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        #heapのサイズがkを超えない場合はそのまま追加し、超える場合は最小値を削除する
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
