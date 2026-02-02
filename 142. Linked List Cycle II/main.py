# まず、サイクルが存在するかを確認する。

# slow は 1 ステップ、fast は 2 ステップずつ進める。
# fast と slow が同じノードを指した場合、サイクルが存在することが分かる。

# slow は 1 ステップ、fast は 2 ステップで進むため、
# 最初に出会った時点で fast は slow よりサイクルを整数回多く回っている状態になっている。

# その後、slow を head に戻し、
# slow と fast をそれぞれ 1 ステップずつ進めると、
# 再び出会うノードがサイクルの開始位置になる。

# ※ 最初に出会った位置からサイクル開始位置までの距離は、
#    head からサイクル開始位置までの距離と等しい。

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # 1단계: 사이클 존재 여부 확인
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # 사이클이 없는 경우
            return None

        # 2단계: 사이클 시작 지점 찾기
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow