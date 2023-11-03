<<<<<<< HEAD
#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
# 給一整數n將其拆解, return總和為n的這些整數們乘積最大的值, 這值要>=2
# Ex: n = 10, 10 = 3+3+4, 3*3*4 = 36

# By DP, time: O(n), space: O(n^2)
# 小數字的最大乘積可以是更大數字之最大乘積的一部份
class Solution:
    def integerBreak(self, n: int) -> int:
        # 初始化dp, dp[i] = n為i時候的解
        dp = [0]*(n+1)
        dp[1] = 1
        # n>=2所以從2開始
        for i in range(2, n + 1):
            # 求最大值所以初始化為負無限下
            dp[i] = float('-inf')
            # 想像當i(也就是n)被拆成j和i-j時, 能夠怎麼拆?
            # 一種情況是直接被拆成兩數j和i-j 另一個情況是i-j被繼續往下拆
            # j是0或i就不叫做拆了, 所以j範圍是1~i-1
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
# @lc code=end

=======
#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
# 給一整數n將其拆解, return總和為n的這些整數們乘積最大的值, 這值要>=2
# Ex: n = 10, 10 = 3+3+4, 3*3*4 = 36

# By DP, time: O(n), space: O(n^2)
# 小數字的最大乘積可以是更大數字之最大乘積的一部份
class Solution:
    def integerBreak(self, n: int) -> int:
        # 初始化dp, dp[i] = n為i時候的解
        dp = [0]*(n+1)
        dp[1] = 1
        # n>=2所以從2開始
        for i in range(2, n + 1):
            # 求最大值所以初始化為負無限下
            dp[i] = float('-inf')
            # 想像當i(也就是n)被拆成j和i-j時, 能夠怎麼拆?
            # 一種情況是直接被拆成兩數j和i-j 另一個情況是i-j被繼續往下拆
            # j是0或i就不叫做拆了, 所以j範圍是1~i-1
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
# @lc code=end

>>>>>>> 6861f1229a47360993e49170b9b1be7c1dd4f215
