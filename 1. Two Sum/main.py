# hash mapを使用して問題を解決する。
# hash mapは要素をkeyとvalueのペアで保存し、高速な探索を可能にする。
# 本問題ではindexを返す必要があるため、
# 要素の値をkey、indexをvalueとして保存する。

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target - nums[i]], i]
            hash_map[nums[i]] = i
        return []