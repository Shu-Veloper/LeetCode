# min_priceの初期値をpricesの最初の値に設定（最初の日に買うと仮定）
# すでにprices[0]を考慮しているため、for文は1から開始する
# 各日について、これまでの最小価格で買って今日売った場合の利益を計算する
# if文でmin_priceを更新し、更新されなかった場合にelifでprofitを更新する
# 計算した利益が現在のprofitより大きければ更新する
# 最終的に最大利益であるprofitを返す

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif profit < prices[i] - min_price:
                profit = prices[i] - min_price
        return profit
