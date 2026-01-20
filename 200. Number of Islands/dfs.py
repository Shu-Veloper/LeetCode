# DFS - Depth-First Search = stack(LIFO) / 再帰
# 再帰とは、関数が自分自身を呼び出す仕組みのことです。
# 再帰の中に終了条件を設けることで、無限ループを防ぎます。
# 再帰を使うことで、スタックを用いた探索を簡潔に実装できます。stack(LIFO)
# codingtestによく出る問題例：
# - 連携された領域(Connected Components)を探索する問題
# - 島(Number of Islands) 問題
# - 上下左右に移動して隣接する'1'を訪問済みにマークする問題
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])
        # 再帰関数i,jの周りの'1'を'0'に変える
        def dfs(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            # 下に移動する
            dfs(i+1,j)
            # 上に移動する
            dfs(i-1,j)
            # 右に移動する
            dfs(i,j+1)
            # 左に移動する
            dfs(i,j-1)
        for i in range(col):
            for j in range(row):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        return count