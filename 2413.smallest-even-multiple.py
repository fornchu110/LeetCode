#
# @lc app=leetcode id=2413 lang=python3
#
# [2413] Smallest Even Multiple
#

# @lc code=start
# By mod, time: O(1), space: O(1)
# 給定n, return n和2的最小公倍數
# 也就是說只要n是偶數就回傳自己, n是奇數就回傳n*2
# 可以利用位運算或對n%2結果作處理加快程式碼速度
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            # n<<1代表n左移一bit, 等同乘以2
            return n<<1
# @lc code=end

