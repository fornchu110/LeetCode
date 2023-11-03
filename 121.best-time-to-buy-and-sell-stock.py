#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
# By DP
#假設在第i天賣出, 那在這i天內的最低點購買就有最大收益
#i天內的歷史最低點, 只有可能是第i-1天時的最低點或第i天的價格兩種
#因此可寫成動態規劃
#i天買i天賣沒意義, 所以歷史最低點是在算完收益後再更新
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

# @lc code=end

