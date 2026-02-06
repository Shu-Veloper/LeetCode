# 考え方として、left と right の2つのポインタを設定し、
# 文字列の両端から文字を比較していきます。

# left と right の文字が一致している場合は、
# それぞれ left をインクリメント、right をデクリメントして次に進みます。

# 文字が一致しなかった場合は、
# 一度だけ文字を削除したと仮定し、
# [left + 1 から right] または [left から right - 1] の範囲が
# 回文かどうかを確認します。

# その過程ですべて一致すれば True を返し、
# どちらも回文でなければ False を返します。

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1

        return True