#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
# By int(max()), time: O(n), space: O(1)
# 事實上就是找給定數n的每位數中最大的數, 因較小的部分補0即可
class Solution:
    def minPartitions(self, n: str) -> int:
        # max在input字串時, 會找字串中ascii碼最大的字元
        # 找到後再用int()將字元轉換成整數
        return int(max(n))

# @lc code=end

