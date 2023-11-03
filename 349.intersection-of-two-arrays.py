#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start

# By set
# 轉換成set可以將重複元素刪掉, 但沒有index
# 可以用list()再轉成list有index, 但花時間
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 解答陣列
        res = list()
        set1 = set(nums1)
        set2 = set(nums2)
        # 選擇走訪長度比較短的set
        if(len(set1)<len(set2)):
            # 每次看set中一個元素, 當下看的定為i
            for i in set1:
                # 只要set1的i也在set2裡面, 加入res
                if i in set2:
                    res.append(i)
        # 同理
        else:
            for i in set2:
                if i in set1:
                    res.append(i)
        return res

# By double pointer
# 先排序再比對, 一樣的話加入, 還要確保答案內元素的唯一性
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()
#         length1, length2 = len(nums1), len(nums2)
#         intersection = list()
#         index1 = index2 = 0
#         while index1 < length1 and index2 < length2:
#             num1 = nums1[index1]
#             num2 = nums2[index2]
#             if num1 == num2:
#                 # 需要不重複才加入intersection
#                 if not intersection or num1 != intersection[-1]:
#                     intersection.append(num1)
#                 index1 += 1
#                 index2 += 1
#             elif num1 < num2:
#                 index1 += 1
#             else:
#                 index2 += 1
#         return intersection




# @lc code=end

