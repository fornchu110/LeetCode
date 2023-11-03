#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
# 給n, n為一等差陣列1, 3, 5, ...的元素數量
# 定義一次操作將一個元素-1一個元素+1
# return 經過最少次操作能讓陣列內元素都相等

# By greedy, time: O(n), space: O(n), 不將陣列模擬出來的話是space: O(1)
# 求出平均值後, 看比平均值小的數與平均值的差值總和即是答案
# 其實平均值就是原本給的n, 所以找2*i+1與n的差值即可, 看要大於還小於
class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        # 模擬出陣列的做法
        # arr = []
        # for i in range(n):
        #     arr.append(2*i+1)
        # average = arr[0]+arr[len(arr)-1]//2
        # for i in range(len(arr)//2):
        #     res += average-arr[i]
        # return res
        # 不用模擬陣列的做法, space: O(1)
        for i in range(n):
            if (2*i+1)<n:
                res += n-(2*i+1)
        return res
        # 一行版
        # return sum(x - n for i in range(n) if (x := 2 * i + 1) > n)

# By math, time: O(1), space: O(1)
# 經過數學推導可知答案與n的關係
# class Solution:
#     def minOperations(self, n: int) -> int:
#         # 記得加減乘除的優先權比位移高
#         return n*n>>2

# @lc code=end

