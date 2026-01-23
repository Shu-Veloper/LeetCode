# Two Pointersの問題
# 左右からポインタを動かし、英数字のみを比較する
# while start < end を条件にして無限ループを防ぐ
# isalnum() は文字または数字かどうかを判定するメソッド
# 比較して一致すれば、左右のポインタをそれぞれ内側に移動する

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True