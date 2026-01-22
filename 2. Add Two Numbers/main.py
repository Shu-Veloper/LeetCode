# linkedlistの使い方を確認するためのコード                                                                                                    
# linkedlistに値を追加する際に、nextを指定しないといけない。                                                                                  
# 追加した後nextでpointerを進める必要がある。                                                                                                 
# 問題の解決思考                                                                                                                              
# ListNodeを作成して、l1,l2の値を桁ごとに足し合わせる                                                                                         
# リンクリストは逆順（1の位から順）で格納されているので、先頭から順に足し合わせれば良い                                                       
# ＊桁上がりを考慮して,carry,digitを用意する                                                                                                  
# linkedlist,pointerの進め方に注意する


# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            # ノード単位の値を取得して足し合わせる
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            # 桁上がりを考慮してcarryとdigitを計算する
            # carryは10以上の場合1、そうでない場合0
            carry = total // 10
            # digitは10未満の値
            digit = total % 10
            # 新しいノードを作成してcurrentのnextに追加する
            current.next = ListNode(digit)
            # pointerを進める
            current = current.next
            # l1,l2のpointerを進める
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next