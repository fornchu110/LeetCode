#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start

# By set
# �ഫ��set�i�H�N���Ƥ����R��, ���S��index
# �i�H��list()�A�নlist��index, ����ɶ�
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # �ѵ��}�C
        res = list()
        set1 = set(nums1)
        set2 = set(nums2)
        # ��ܨ��X���פ���u��set
        if(len(set1)<len(set2)):
            # �C����set���@�Ӥ���, ��U�ݪ��w��i
            for i in set1:
                # �u�nset1��i�]�bset2�̭�, �[�Jres
                if i in set2:
                    res.append(i)
        # �P�z
        else:
            for i in set2:
                if i in set1:
                    res.append(i)
        return res

# By double pointer
# ���ƧǦA���, �@�˪��ܥ[�J, �٭n�T�O���פ��������ߤ@��
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
#                 # �ݭn�����Ƥ~�[�Jintersection
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

