#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
# 給一list gain代表不同高度, 假設都以高度0出發, 接著依序走訪gain中不同相對高度
# return走訪過程中最高點所在
# Ex: gain = [-5, 1, 5, 0, -7], 0 -> -5 -> -4 -> 1 -> 1 -> -6, 所以最高點在1

# By for loop, time: O(n), space: O(1)
# 走訪gain過程做+運算即可知道當下高度, 在高於目前最高高度res時更新
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tmp = 0
        res = 0
        for i in gain:
            tmp += i
            # 下面等同res = max(tmp, res)
            if tmp>res:
                res = tmp
        return res

# @lc code=end

