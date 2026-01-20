# BFS - Breadth-First Search = queue(FIFO) / キュー
# キューとは、先入れ先出し（FIFO: First In First Out）のデータ構造です。
# キューを使うことで、幅優先探索を効率的に実装できます。
# codingtestによく出る問題例
# - 連携された領域(Connected Components)を探索する問題
# - 島(Number of Islands) 問題
# - 上下左右に移動して隣接する'1'を訪問済みにマークする問題
# - 最短経路問題(Shortest Path Problems)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows = len(grid)
        cols = len(grid[0]) 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    # 現在の位置を保存する
                    queue = [(i,j)]
                    # countされないように'0'に変える
                    grid[i][j] = '0'
                    # 上記を含めた'1'に隣接する'1'をすべて探索する
                    while queue:
                        x,y = queue.pop(0)
                        for k in range(len(dx)):
                            # 右、左、下、上に移動する　
                            nx = x + dx[k]
                            ny = y + dy[k]
                            # 範囲外の場合はスキップ
                            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                              continue
                            # '0'の場合はスキップ
                            if grid[nx][ny] == '0':
                              continue
                            # '1'の場合はキューに追加し、'0'に変える
                            queue.append((nx, ny))
                            grid[nx][ny] = '0'
        return count
        