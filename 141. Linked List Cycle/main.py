# Linked Listの仕組みを利用し、うさぎとかめアルゴリズム（Floydの循環検出法）を用いて、
# リストにcycle（循環）が存在するかどうかを判定するコードである。
# fastポインタは一度に2ノード進み、slowポインタは一度に1ノード進む。
# cycleが存在する場合、最終的にfastポインタとslowポインタは同じノードを指す。

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False