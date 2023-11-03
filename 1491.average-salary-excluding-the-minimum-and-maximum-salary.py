#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
# 給一個陣列salary, 將最大值和最小值去除後, return剩下這些元素的平均值並取到小數後5位
# 並不要求小數點, 世說誤差在10^-5次方內都算對

# By min() and max(), time: O(n), space: O(1)
# 直接用min()和max()找最大最小值, 先將salary元素加總減掉這兩者即可
class Solution:
    def average(self, salary: List[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        total = sum(salary) - maxValue-minValue
        return total/(len(salary)-2)

# By sort and deque, time: O(n), space: O(n)
# 利用collections.deque()製作雙邊queue, 將sort後的salary尾端和頭端元素pop出, 也就是最大最小值
# 再對剩下元素加總取平均, 並用round取到小數點後五位
# class Solution:
#     def average(self, salary: List[int]) -> float:
#         salary.sort()
#         queue = collections.deque()
#         for i in salary:
#             queue.append(i)
#         queue.pop()
#         queue.popleft()
#         res = 0
#         for i in queue:
#             res += i
#         res /= len(queue)
#         # round第二個參數是小數點位數, 若要res變str用format(res, %.5f)
#         # res = round(res, 5)
#         return res
# @lc code=end

