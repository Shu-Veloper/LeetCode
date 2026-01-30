# リストを順番にチェックしながら、出現した値を set に保存する。
# set は O(1) で存在確認ができるため、同じ値が再び出てきた場合は重複と判断して True を返す。
# すべて確認しても重複がなければ False を返す。

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            set_nums.add(i)
        return False