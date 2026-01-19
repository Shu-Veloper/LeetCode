# hashmapを利用してアナグラムをグループ化するPythonコードです。
# アナグラムとは、同じ文字を使って異なる順序で構成された単語のことを指します。
# 例えば、「eat」と「tea」はアナグラムの関係にあります。
# 手順：
# 1. 各単語をソートして、そのソートされた文字列をキーとして使用します。
# 2. ハッシュマップにそのキーが存在する場合は、対応するリストに単語を追加します。
# 3. 存在しない場合は、新しいリストを作成して単語を追加します。
# 4. 最終的に、ハッシュマップの値をリストとして返します。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return list(hash_map.values())
