#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
# 將比pivot小的元素放在pivot左邊, 比pivot大的元素放在pivot右邊, 同時要照個原本的先後順序不能混淆(要求index stable)
# By double pointer, time: O(n), space: O(1), res不算額外空間
# 一開始left和right指向最左最右端, 走訪nums時小於的放left, 大於的放right並改變更新index
# 大於的部分並沒照著index順序(因為是從右而左放的), 所以要重新翻轉
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot] * n
        # 小於的部分從左而右, 大於的部分從右而左
        left, right = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
            elif nums[i] > pivot:
                res[right] = nums[i]
                right -= 1
        # 翻轉大於的部分
        x, y = right+1, n-1
        while x < y:
            res[x], res[y] = res[y], res[x]
            x += 1
            y -= 1
        
        return res

# By partition, time: O(n), space: O(n)
# 分成三個部分最後再合而為一即可, 但多花空間
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         left = []
#         mid = []
#         right = []
#         res = []
#         for i in nums:
#             if i<pivot:
#                 left.append(i)
#             elif i==pivot:
#                 mid.append(i)
#             else:
#                 right.append(i)
#         for i in left:
#             res.append(i)
#         for i in mid:
#             res.append(i)
#         for i in right:
#             res.append(i)
#         return res

# @lc code=end

