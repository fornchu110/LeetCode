#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
# By hash table, time: O(m+n), space: O(m), m是jewles長度, n是stones長度
# 要看jewels內的字符共在jewels內出現幾次
# 先將jewels內容走訪一次加入hash table, 又再走訪一次stone看次數
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        # set在python是hast table的一種, 不會有重複元素
        # 可以用add和remove, 不像list用append加入
        jewelsSet = set(jewels)
        for i in stones:
            if i in jewelsSet:
                res += 1
        return res

# By for loop, time: O(m*n), space: O(1), m是jewles長度, n是stones長度
# 要看jewels內的字符共在jewels內出現幾次
# 這種寫法每次走訪stones內容都回去jewels走訪一遍, 所以是m*n
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         res = 0
#         for i in stones:
#             if i in jewels:
#                 res += 1
#         return res

# @lc code=end
