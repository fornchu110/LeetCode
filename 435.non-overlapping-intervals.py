#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
# 給一陣列intervals內有多個區間, 要求return刪除最小數區間使這些區間都不重疊
# 注意要根據題目舉例判斷區間是開區間還是閉區間, 之前滿多閉區間, 但這題是開區間
# Ex: [1, 2], [2, 3]並沒有重疊, 也就是non-overlapping

# By greedy, time: O(nlogn), space: O(logn)
# space = O(logn)是因sort()所要花費的空間
# 想法是將區間根據上界排序, 所以說上界越低的區間越早結束, 就留有更大的範圍跟其他區間
# 若要作區間以下界排序的寫法, 則要在重疊的區間中找上界較低者作為留下來的區間
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 邊界條件, 當intervals內沒有區間, 代表不用刪除return 0
        if len(intervals) == 0:
            return 0
        # 用key = lambda x: x[1]來根據上界排序
        intervals.sort(key=lambda x: x[1])
        # cnt為不重疊的區間數, 在至少有一個區間的情況下初始為1
        cnt = 1
        # end是要比較的上界, 初始化為第0個區間的上界
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # 當上一個結束的區間上界<=目前區間的下界, 代表不會重疊
            if end <= intervals[i][0]:
                # 不重疊區間數+1
                cnt += 1
                # 將這次的區間上界更新為結束的區間上界, 給下個區間比較
                end = intervals[i][1]
        # 區間總數-不重複區間數=重複區間數, 也就是要刪除的區間數量
        return len(intervals)-cnt

# @lc code=end

