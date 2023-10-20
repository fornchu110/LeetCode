#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start

# By hash table, time: O(m+n), m�Onums1����, n�Onums2����
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        # ���ݭn�ب������, 
        hashtable1 = dict()
        for x in nums1:
            if x in hashtable1:
                hashtable1[x] += 1
            else:
                hashtable1[x] = 1
        # �Nnums1���������[�Jhashtable��
        # �������Xnums2
        # �îھ�hashtable�����F��P�_�O�_�n�Nnums2�����[�Jres
        for x in nums2:
            if x in hashtable1 and hashtable1[x]>0:
                res.append(x)
                hashtable1[x] -= 1
        return res
            
# By set and index array, ���������O�Ŷ��ɶ�, �h�F�ĤT���j��
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
# �����Ъ����k�n�binput�ƧǦn�����p�ϥ�, �ҥH��sort
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

