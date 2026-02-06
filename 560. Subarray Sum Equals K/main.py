# prefix_sum[x] は nums[0] から nums[x] までの累積和。

# ある区間 i〜j の和が k のとき、
# prefix[j] - prefix[i-1] = k が成り立つ。

# prefix[j] には 0〜j まで全て含まれているため、
# 不要な前半部分 prefix[i-1] を引くことで
# 区間 i〜j の和を求めることができる。

# この式を変形すると、
# prefix[j] - k = prefix[i-1] となり、
# 「過去に prefix[j] - k の累積和が存在すれば、
# その直後から j までの区間の和は k」
# という意味になる。

# そのため、HashMap に
# key: 累積和
# value: 出現回数
# を保存する。

# {0:1} を最初に入れるのは、
# 何も足していない状態（累積和0）が
# 1回存在すると考えるため。


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {}
        prefix_count[0] = 1
        cur_sum = 0
        answer = 0
        for i in nums:
            cur_sum += i
            target = cur_sum - k
            if target in prefix_count:
                answer += prefix_count[target]
            prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1
        return answer
