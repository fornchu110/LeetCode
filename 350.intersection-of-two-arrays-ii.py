#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start

# By hash table, time: O(m+n), m是nums1長度, n是nums2長度
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        # 不需要建兩個雜湊, 
        hashtable1 = dict()
        for x in nums1:
            if x in hashtable1:
                hashtable1[x] += 1
            else:
                hashtable1[x] = 1
        # 將nums1內的元素加入hashtable後
        # 直接走訪nums2
        # 並根據hashtable內的東西判斷是否要將nums2元素加入res
        for x in nums2:
            if x in hashtable1 and hashtable1[x]>0:
                res.append(x)
                hashtable1[x] -= 1
        return res
            
# By set and index array, 比雜湊表浪費空間時間, 多了第三次迴圈
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         res = list()
#         upper = max(max(nums1), max(nums2))
#         freq1 = [0] * (upper+1)
#         freq2 = [0] * (upper+1)
#         for x in nums1:
#             freq1[x] += 1
#         for x in nums2:
#             freq2[x] += 1
#         set1 = set(nums1)
#         for x in set1:
#             if freq1[x]<freq2[x]:
#                 while freq1[x]!=0:
#                     res.append(x)
#                     freq1[x] -=  1
#             else:
#                 while freq2[x]!=0:
#                     res.append(x)
#                     freq2[x] -= 1
#         return res

# By double pointer
# 雙指標的做法要在input排序好的情況使用, 所以先sort
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1.sort()
#         nums2.sort()

#         length1, length2 = len(nums1), len(nums2)
#         intersection = list()
#         index1 = index2 = 0
#         while index1 < length1 and index2 < length2:
#             if nums1[index1] < nums2[index2]:
#                 index1 += 1
#             elif nums1[index1] > nums2[index2]:
#                 index2 += 1
#             else:
#                 intersection.append(nums1[index1])
#                 index1 += 1
#                 index2 += 1
        
#         return intersection

# @lc code=end

