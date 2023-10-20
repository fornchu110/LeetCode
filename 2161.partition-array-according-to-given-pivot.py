#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
# �N��pivot�p��������bpivot����, ��pivot�j��������bpivot�k��, �P�ɭn�ӭӭ쥻�����ᶶ�Ǥ���V�c(�n�Dindex stable)
# By double pointer, time: O(n), space: O(1), res�����B�~�Ŷ�
# �@�}�lleft�Mright���V�̥��̥k��, ���Xnums�ɤp�󪺩�left, �j�󪺩�right�ç��ܧ�sindex
# �j�󪺳����èS�ӵ�index����(�]���O�q�k�ӥ���), �ҥH�n���s½��
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [pivot] * n
        # �p�󪺳����q���ӥk, �j�󪺳����q�k�ӥ�
        left, right = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
            elif nums[i] > pivot:
                res[right] = nums[i]
                right -= 1
        # ½��j�󪺳���
        x, y = right+1, n-1
        while x < y:
            res[x], res[y] = res[y], res[x]
            x += 1
            y -= 1
        
        return res

# By partition, time: O(n), space: O(n)
# �����T�ӳ����̫�A�X�Ӭ��@�Y�i, ���h��Ŷ�
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

