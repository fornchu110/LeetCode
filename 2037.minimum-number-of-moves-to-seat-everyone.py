#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
# 給一陣列seats和students, seats[i]和students[i]代表第i個的位置
# 一次只能移動student一個位置, 問將所有student各分配到一個seat的最小移動次數
# 一開始也可能會有多個student在同個位置

# By sort, time: O(nlogn), space: O(logn), space = O(logn)是排序所花費的stack空間
# 將seats和student都排序過後一一相減即可
# 排序所代表的是將學生移動到離自己最近的位置
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        # 用zip同時走訪兩個不同陣列的相同index之元素, i、j分別代表當下index在該陣列的元素
        for i, j in zip(seats, students):
            res += abs(i-j)
        return res

# @lc code=end

