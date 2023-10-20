#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
# By pair, time: O(n), space: O(1)
# 給字串s, 問可以分成幾個R和L數量相同的子字串
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        # 紀錄有多少R
        cnt = 0
        # 從頭看到尾, 有R+1有L-1, 當0時代表R和L數量相同
        for i in s:
            if i=='R':
                cnt += 1
            elif i=='L':
                cnt -= 1
            if cnt==0:
                res += 1
        return res

# @lc code=end

