# 最初のループで各位置 i に「左側すべての要素の積」を格納し、
# 次のループで「右側すべての要素の積」を掛け合わせることで、
# nums[i] を除いた積を求める。

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = [1] * length

        left = 1
        for i in range(length):
            arr[i] = left
            left *= nums[i]

        right = 1
        for i in range(length - 1, -1, -1):
            arr[i] *= right
            right *= nums[i]

        return arr

