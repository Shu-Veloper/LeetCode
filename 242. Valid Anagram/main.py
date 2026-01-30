# アナグラムの場合、まず文字数が同じである必要がある。
# Counter 関数を使うと、各文字の出現回数をカウントできる。
# 2つの文字列のカウント結果が一致すれば True、一致しなければ False を返す。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False