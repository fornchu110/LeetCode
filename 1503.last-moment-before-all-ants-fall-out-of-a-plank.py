#
# @lc app=leetcode id=1503 lang=python3
#
# [1503] Last Moment Before All Ants Fall Out of a Plank
#

# @lc code=start
# 給路徑長n和往left走的螞蟻起始index以及往right走的螞蟻起始index
# return多久時間以後, 所有螞蟻能走完離開路徑長為n的path(此path有0~n共n+1個index)

# By greedy, time: O(n), space: O(1)
# 無論往左走往右走一次都走一格
# 所有螞蟻能走完的時間等同於要走最久的螞蟻花多少時間, 就等同找螞蟻要走的最長路徑
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for i in right:
            res = max(res, n-i)
        for i in left:
            res = max(res, i)
        return res
        
# @lc code=end

