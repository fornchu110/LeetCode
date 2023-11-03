<<<<<<< HEAD
#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
# By for loop, time: O(m*n), space: O(1)
# 要出找一維陣列內元素和最大的, 有m個一維陣列, 每個一維陣列n個元素
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        # len(accounts)就等同一維陣列數量
        for i in range(len(accounts)):
            tmp = 0
            # len(accounts[i])就等同第i個一維陣列內的元素數量
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            if tmp>max:
                max = tmp
        # 程式可以只有下面這row
        #return max(map(sum, accounts))
        return max

# @lc code=end

=======
#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
# By for loop, time: O(m*n), space: O(1)
# 要出找一維陣列內元素和最大的, 有m個一維陣列, 每個一維陣列n個元素
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        # len(accounts)就等同一維陣列數量
        for i in range(len(accounts)):
            tmp = 0
            # len(accounts[i])就等同第i個一維陣列內的元素數量
            for j in range(len(accounts[i])):
                tmp += accounts[i][j]
            if tmp>max:
                max = tmp
        # 程式可以只有下面這row
        #return max(map(sum, accounts))
        return max

# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
