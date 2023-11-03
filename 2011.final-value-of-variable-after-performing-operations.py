#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
# By string compartion, time: O(n), space: O(1)
# 對list中每個字串做比較, 只有X++, ++X , X--, --X四種可能
# 前兩者x += 1, 後兩者x -= 1即可
# 更精準的方式是只判斷list中字串中間那個符號, 必為+或-
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            # 直接判斷的方式
            # if i=="X++" or i=="++X":
            # 更精準判斷i[1]必為+或-
            if i[1]=="+":
                x += 1
            else:
                x -= 1
        return x 
        
# @lc code=end

