# 解説：two pointers + set

# まず、重複を防ぐために set を用意する。
# 次に two pointers（left, right）を使って文字列を走査する。

# right ポインタを右に動かしながら、
# 現在の文字が set に含まれているかを確認する。

# もし while s[right] in seen の状態になった場合、
# 重複がなくなるまで left ポインタを動かし、
# set から左側の文字を1つずつ削除する。

# 重複が解消されたら、
# 現在の文字を set に追加し、
# right - left + 1 で現在の部分文字列の長さを計算する。

# max 関数を使って、
# これまでの最大長を max_len に記録する。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len